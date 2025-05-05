
AI Insight Chatbot - README
============================


Table of Contents
-----------------
- Introduction
- Project Architecture
- Backend Development
- Frontend Development (Streamlit)
- Deployment
- Screenshots
- Future Enhancements
- Contributors

Introduction
------------
The AI Insight Chatbot answers business-related questions by analyzing a Sales Dataset (10,000 rows × 26 columns).
It combines:
- Local Data Processing (Pandas)
- Generative AI (Gemini 1.5 Flash Model) for natural responses
- Streamlit Frontend
- Flask API Backend

Project Architecture
---------------------
User → Streamlit Frontend → Flask Backend → Local Data Processing (Pandas) → Gemini Model → Response

Backend Development
--------------------
Folder: /backend

Tech Stack:
- Python 3.9+
- Flask
- Pandas
- Google's Gemini Model (via genai library)

Folder Structure:
/backend
    ├── app.py
    ├── requirements.txt
    ├── data/
    │     └── sales_data.csv

Main Backend Code (app.py):

- Flask app setup.
- Load sales data (sales_data.csv).
- Local processing using Pandas for common queries.
- Send summary + user query to Gemini model.
- Return the final refined response.

Frontend Development (Streamlit)
---------------------------------
Folder: /frontend

Tech Stack:
- Streamlit
- Requests

Folder Structure:
/frontend
    ├── app.py
    ├── requirements.txt
    └── assets/
          └── logo.png (optional)

Main Frontend Code (app.py):

- Streamlit app setup with user input box.
- Sends user queries to backend API (/ask).
- Displays AI responses beautifully.

Deployment
----------
Backend:
    cd backend
    pip install -r requirements.txt
    python app.py

Frontend:
    cd frontend
    pip install -r requirements.txt
    streamlit run app.py

Ports:
- Backend (Flask): http://localhost:5000
- Frontend (Streamlit): http://localhost:8501

Screenshots
-----------
[Insert Streamlit Interface Screenshot Here]

Future Enhancements
-------------------
- Smarter query understanding.
- Model switching feature.
- Visualization charts and graphs.
- Authentication system.
- Dockerize full project.

Contributors
------------
- Your Name Here

Quick Start
-----------
# Backend
cd backend
pip install -r requirements.txt
python app.py

# Frontend
cd frontend
pip install -r requirements.txt
streamlit run app.py

Important Notes
---------------
- Ensure sales_data.csv is loaded properly.
- Secure the Gemini API Key.
- Always run backend before frontend.
