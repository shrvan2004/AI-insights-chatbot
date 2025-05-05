import requests
import json

# URL of the backend
url = "http://127.0.0.1:5000/ask"

# Sample query to test the chatbot on large dataset
query = {
    "query": "Which category has the highest total sales?"
}

# Send request
response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(query))

# Print response
if response.status_code == 200:
    print("Chatbot Response:")
    print(response.json()["response"])
else:
    print(f"Error: Status Code {response.status_code}")
    print("Response Text:", response.text)
