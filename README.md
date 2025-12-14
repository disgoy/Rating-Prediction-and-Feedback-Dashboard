# ⭐ AI Rating Prediction & Feedback System

## Overview
This project demonstrates how **Large Language Models (LLMs)** can be used for:
1. **Rating prediction via prompt engineering (Task 1)**
2. **A deployed, two-dashboard AI feedback system (Task 2)**

The focus is on **prompt design, reliability, system behavior, and deployment**, without any model fine-tuning.

---

## Task 1 — Yelp Rating Prediction (Prompt Engineering)

**Goal:**  
Predict Yelp review star ratings (1–5) using **prompt engineering only** and analyze how prompt design impacts accuracy and output reliability.

**Highlights**
- Dataset: Yelp Reviews (Kaggle)
- Model: `mistralai/mistral-7b-instruct` (via OpenRouter)
- Prompt iterations:
  - v1: Naive baseline
  - v2: Strict JSON enforcement
  - v3.3: Accuracy-optimized (domain rubric)
  - v3.4: JSON-reliability optimized
- Evaluation:
  - Accuracy vs ground truth
  - JSON validity rate

**Key Insight:**  
Stricter prompts improve reliability, while domain-aware prompts improve accuracy—often with trade-offs.

📄 `Task1.ipynb`

---

## Task 2 — AI Feedback System (Deployed)

**Goal:**  
Build and deploy a **web-based AI feedback system** with separate user and admin views.

**Features**
- **User Dashboard:** Submit rating + review, receive AI-generated response
- **Admin Dashboard:** View all submissions with AI summaries and recommended actions
- Shared datastore across dashboards

**Design**
- Streamlit multipage app (single deployment, multiple endpoints)
- CSV-based shared storage
- LLM-powered:
  - User responses
  - Review summaries
  - Business action recommendations

**Reliability**
- Separate prompt styles for user vs admin outputs
- Output sanitization for model artifacts
- Rule-based fallbacks for short or low-context reviews

**Deployment**
- Streamlit Community Cloud
- Secure API key handling via secrets
- Publicly accessible dashboards

---

## Tech Stack
- LLM: OpenRouter (`mistralai/mistral-7b-instruct`)
- Frontend: Streamlit
- Backend: Python
- Storage: CSV
- Deployment: Streamlit Cloud
