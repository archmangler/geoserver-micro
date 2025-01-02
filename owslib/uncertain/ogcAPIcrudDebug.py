import requests

url = 'http://localhost:8080/geoserver'  # Make sure this is the correct endpoint for Records
response = requests.get(url)

# Print the status code and content of the response
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")

# Check if the content is JSON before parsing
if response.headers.get('Content-Type') == 'application/json':
 data = response.json()
else:
 print("Response is not in JSON format.")
