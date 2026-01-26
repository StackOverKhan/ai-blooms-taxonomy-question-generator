# AI-Powered Bloom’s Taxonomy Question Generator

## 🚀 Overview
An AI-powered web application that generates exam questions aligned with Bloom’s Taxonomy cognitive levels.  
It helps educators design outcome-oriented, higher-quality assessments instead of memory-based questions.

## 🎯 Features
- Subject and topic-based question generation
- Bloom’s Taxonomy cognitive level selection
- Outcome-oriented exam questions
- Real-time AI generation using Google Gemini
- Clean and intuitive web interface

## 🛠️ Tech Stack
- Python 3.11
- Streamlit
- Google Gemini API

## 🤖 Google Technologies Used
- Google Gemini (Flash / Lite) for content generation

## ⚙️ How It Works
1. User enters subject and topic
2. User selects Bloom’s Taxonomy level
3. Request is sent to Gemini AI
4. AI generates 5 outcome-based questions
5. Questions are displayed instantly

## ▶️ Run Locally
```bash
pip install streamlit google-generativeai
setx GEMINI_API_KEY "your_api_key_here"
py -3.11 -m streamlit run app.py

```
## 🔮 Future Enhancements
- Answer generation toggle
- MCQ / Long / Short answer modes
- Export questions to PDF / DOC
- Question bank integration
- CO–PO mapping for academic assessment
