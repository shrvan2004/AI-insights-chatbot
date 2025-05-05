import streamlit as st
import requests

st.set_page_config(page_title="AI Insight Chatbot", layout="wide")
st.title("📊 AI Insight Chatbot - Sales Data Analysis")

st.markdown("Ask your questions related to the sales dataset (10,000 rows × 26 columns).")

user_query = st.text_input("Enter your query below:")

if st.button("Ask Chatbot"):
    if user_query.strip() == "":
        st.warning("Please enter a query before submitting.")
    else:
        try:
            response = requests.post(
                url="http://127.0.0.1:5000/ask",
                headers={"Content-Type": "application/json"},
                json={"query": user_query}
            )
            if response.status_code == 200:
                result = response.json()
                st.success(result["response"])
            else:
                st.error(f"Backend Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Error occurred: {str(e)}")
