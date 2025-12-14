import streamlit as st
import os
import requests
import csv
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Feedback System", layout="wide")

# Sidebar Navigation
page = st.sidebar.selectbox("Select Dashboard", ["User Dashboard", "Admin Dashboard"])

DATA_FILE = "feedback_data.csv"

SHORT_POSITIVE_WORDS = [
    "amazing", "great", "awesome", "excellent", "good", "nice", "love", "perfect"
]

# ---------------- USER DASHBOARD ----------------
if page == "User Dashboard":
    st.title("⭐ Customer Feedback Portal")

    rating = st.selectbox("Select Star Rating", [1, 2, 3, 4, 5])
    review = st.text_area("Write your review", placeholder="Type your experience here...")

    if st.button("Submit Review"):
        if review.strip() == "":
            st.warning("Please write a review before submitting.")
        else:
            st.info("Generating AI outputs...")

            API_KEY = os.getenv("OPENROUTER_API_KEY")
            url = "https://openrouter.ai/api/v1/chat/completions"

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "AI Feedback System"
            }

            def call_llm(prompt):
                data = {
                    "model": "mistralai/mistral-7b-instruct",
                    "messages": [
                        {
                            "role": "system",
                            "content": (
                                "You are a helpful business analyst AI. "
                                "Give clear, complete, human-readable answers."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": 0.6,
                    "max_tokens": 200
                }

                response = requests.post(url, headers=headers, json=data)
                result = response.json()

                try:
                    text = result["choices"][0]["message"]["content"]

                    # Clean common model artifacts
                    for token in ["<s>", "</s>", "[OUT]", "[/OUT]", "[B_INST]", "[/B_INST]"]:
                        text = text.replace(token, "")


                    text = text.strip()

                    if text == "":
                        return "No meaningful response generated."

                    return text


                except Exception as e:
                    return f"Error generating response: {e}"


            ai_response = call_llm(
                f"""
                You are a customer support representative for a food business.

                A customer left a {rating}-star review saying:
                "{review}"

                Write a warm, natural, human-sounding reply.
                Be empathetic and appreciative.
                Do NOT mention internal processes.
                Do NOT sound like an AI.
                Even if the review is short, try to write a response according to the review sentiment.
                Try your best to respond appropriately based on the star rating.
                Try your best to respond to the customer review content.
                """
            )

            # Fallback override for very short positive reviews
            clean_review = review.lower().strip()

            if (
                len(clean_review.split()) <= 2
                and any(word in clean_review for word in SHORT_POSITIVE_WORDS)
            ):
                ai_response = "Thank you for your feedback! We’re glad you had a great experience."

            ai_summary = call_llm(
                f"""
                Review:
                "{review}"

                Task:
                Write a single-sentence summary capturing the customer's main sentiment and concern.
                Make sure to give a concise and clear summary, do NOT leave it empty or say No meaningful response generated.
                """
            )

            ai_action = call_llm(
                f"""
                You are a business operations assistant.

                Customer review:
                "{review}"

                Choose the MOST appropriate action from the list below and rewrite it in your own words:

                - Improve food quality
                - Adjust seasoning or ingredients
                - Improve service speed
                - Train staff
                - Follow up with the customer
                - No action required

                Rules:
                - Respond with ONE clear sentence
                - Do NOT explain your choice
                - Do NOT use bullet points
                """
            )

            with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([
                    datetime.now().isoformat(),
                    rating,
                    review,
                    ai_response,
                    ai_summary,
                    ai_action
                ])

            st.success("Feedback submitted successfully!")
            st.subheader("AI Response to You")
            st.write(ai_response)

# ---------------- ADMIN DASHBOARD ----------------
if page == "Admin Dashboard":
    st.title("🛠 Admin Dashboard")

    if not os.path.exists(DATA_FILE):
        st.warning("No feedback data available yet.")
    else:
        df = pd.read_csv(DATA_FILE)

        st.subheader("📋 All Customer Feedback")
        st.dataframe(df, use_container_width=True)

        st.subheader("📊 Basic Analytics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Submissions", len(df))

        with col2:
            st.metric("Average Rating", round(df["rating"].mean(), 2))