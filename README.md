# Yelp Rating Prediction using LLM Prompt Engineering

## Overview
This project explores how Large Language Models (LLMs) can be used to predict Yelp review star ratings (1–5) using **prompt engineering only**, without any model fine-tuning.

The task focuses on evaluating how different prompt designs affect:
- Prediction accuracy
- JSON validity
- Reliability and consistency of outputs

## Dataset
- Source: Yelp Reviews Dataset (Kaggle)
- Fields used:
  - Review text
  - Ground-truth star ratings

Due to API latency and free-tier constraints, experiments were conducted on sampled subsets.

## Model & Tools
- LLM Provider: OpenRouter
- Model: mistralai/mistral-7b-instruct
- Environment: Google Colab
- Language: Python

## Prompt Versions
- **v1 (Naive)**: Minimal instructions, baseline behavior
- **v2 (Strict JSON)**: Enforced structured outputs
- **v3.3 (Accuracy-Optimized)**: Added star-rating rubric and user behavior bias
- **v3.4 (JSON-Optimized)**: Restored output reliability with strict formatting

## Evaluation Metrics
- Accuracy (Exact match with ground-truth stars)
- JSON Validity Rate

## Key Findings
- Stricter prompts improve JSON reliability
- Domain-aware prompts improve accuracy
- Accuracy and structured output reliability involve trade-offs

## Files
- `Task1.ipynb`: Complete experiment notebook
