# 🗨 Real-Time Azure OpenAI Chatbot (Python + Flask)

A simple yet powerful real-time chatbot built with **Azure OpenAI (gpt-35-turbo)**, **Python Flask**, and **JavaScript**.  
This project demonstrates how to integrate Azure’s AI models into a web-based interface with conversation memory, token tracking, and cost estimation.

---

## 🚀 Features
- Real-time chatbot interface (Flask + JavaScript)
- Context-aware conversation memory
- Token usage tracking per request
- Easy Azure OpenAI API integration
- Fully customizable UI
- Maintains conversation history across messages
- Shows token usage for transparency
- Cost calculation for each request

---

## 🛠 Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **AI Service:** Azure OpenAI Service (`gpt-35-turbo`)
- **Hosting (Optional):** Azure App Service
- **Version Control:** Git & GitHub

---

 

## 📂 Project Structure

chatbot/
│
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend UI
├── static/
│ ├── style.css # Chat styling
│ └── script.js # Chat frontend logic
├── .env # API keys and configs
└── README.md # Documentation



flowchart TD
    A[User Browser] -->|Types message| B[JavaScript fetch /chat]
    B --> C[Flask Backend]
    C -->|Send message history| D[Azure OpenAI API]
    D -->|AI Reply + Token Usage| C
    C -->|Send reply JSON| B
    B -->|Update UI + Show tokens| A


💰 Cost Estimation
Azure OpenAI charges per 1,000 tokens.

Example for gpt-35-turbo:

Type	Price (per 1K tokens)
Input (Prompt)	$0.0015
Output (Completion)	$0.0020
