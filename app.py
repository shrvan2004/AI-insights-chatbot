from flask import Flask, request, jsonify
import pandas as pd
import google.generativeai as genai     
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)


df = pd.read_csv("https://raw.githubusercontent.com/shrvan2004/AI-insights-chatbot/refs/heads/master/app.py")

app = Flask(__name__)

# Correct Model Setup for v1
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash",
generation_config={"temperature": 0.7,"top_p": 1,"top_k": 32,"max_output_tokens": 2048,}
)



def process_query_locally(query):
    if "highest average sales" in query.lower():
        summary = df.groupby("Product")["Sales"].mean().sort_values(ascending=False).head(5)
        return summary.to_string()
    elif "most profitable region" in query.lower():
        summary = df.groupby("Region")["Profit"].sum().sort_values(ascending=False).head(5)
        return summary.to_string()
    elif "total sales by category" in query.lower():
        summary = df.groupby("Category")["Sales"].sum()
        return summary.to_string()
    else:
        return df.describe(include='all').to_string()

@app.route('/ask', methods=['POST'])
def ask_bot():
    try:
        user_query = request.json.get("query")
        local_summary = process_query_locally(user_query)
        prompt = f"Data Summary:\n{local_summary}\n\nNow answer the user's question: {user_query}"
        
        response = model.generate_content(prompt)
        
        
        final_answer = response.candidates[0].content.parts[0].text.strip()
        return jsonify({"response": final_answer})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
