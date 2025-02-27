import requests


# endpoint = "https://httpbin.org/status/200"
# endpoint1= "https://httpbin.org/anything"
endpoint = "http://localhost:8000/"

response = requests.get(endpoint) #Getting HTTP Request
print(response.status_code)
# print(response.json()) # Json file
# print(response.text) # Print raw html

# Http Request Returns HTML
# REST API HTTP Request returns JSON 
