import requests

url = "http://localhost:8000/api/v1/auth/token/"
data = {
    "email": "test23@example.com",
    "password": "test23",
}
custom_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Frame-Options": "deny",
    "X-Content-Type-Options": "nosniff",
    "X-RateLimit-Limit": "1000",
    "Content-Security-Policy": "default-src 'self'",
    "Access-Control-Allow-Origin": "*",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Allow": "GET, POST, HEAD, OPTIONS",
}

response = requests.post(url, data=data, headers=custom_headers)

print(f"Status_Code: {response.status_code}")
print(f"Body: {response.text}")