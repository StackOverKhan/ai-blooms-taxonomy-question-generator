# AI-Powered Bloom’s Taxonomy Question Generator

## Overview
This project is an AI-powered web application that generates exam questions aligned with Bloom’s Taxonomy cognitive levels. It helps educators create outcome-oriented and pedagogically sound assessments instead of memory-based questions.

The system allows users to select a subject, topic, and Bloom’s level, and instantly generates relevant exam questions using Google Gemini AI.

---

## Features
- Subject and topic-based question generation  
- Bloom’s Taxonomy cognitive level selection  
- Outcome-oriented assessment design  
- Real-time AI-generated exam questions  
- Simple and intuitive web interface  

---

## Technologies Used
- **Python 3.11**
- **Streamlit** – Web application framework
- **Google Gemini API** – AI-powered question generation
- **HTML/CSS (via Streamlit)**

---

## Google Technologies
- **Google Gemini (Gemini 1.5 Flash / Lite)** for real-time content generation

---

## How It Works
1. User enters subject and topic  
2. User selects Bloom’s Taxonomy level  
3. Request is sent to Google Gemini AI  
4. AI generates outcome-based exam questions  
5. Questions are displayed instantly  

---

## Installation & Run
```bash
pip install streamlit google-generativeai
py -3.11 -m streamlit run app.py
