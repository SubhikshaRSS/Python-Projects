# api_service_http.py
#Sending a GET Request
#pip install requests

import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code)
print(response.text)
"""
#Sending a POST Request
import requests
data = {
    "name": "John",
    "age": 30
}
response = requests.post(
    "https://api.example.com/users",
    json=data
)
print(response.status_code)
print(response.json())
"""