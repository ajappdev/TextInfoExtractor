import requests

url = "https://2uxaqebw5j.execute-api.us-east-1.amazonaws.com/diverge/word-info"
data = {"text": "This is a sample text for analysis."}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.json())