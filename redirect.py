import jwt

API_KEY = 'API_KEY'  # Specify your API key
phtoken = 'your_jwt_token_here'  # Replace with the JWT token you want to decode

jwt_response = 0
jwt_phone = ''

try:
    decoded = jwt.decode(phtoken, API_KEY, algorithms=['HS256'])
    jwt_response = 1  # JWT decoded successfully
    jwt_phone = decoded['country_code'] + decoded['phone_no']
except jwt.ExpiredSignatureError:
    jwt_response = 0  # Invalid JWT
except jwt.DecodeError:
    jwt_response = 0  # Invalid JWT

print(f"JWT Response: {jwt_response}")
print(f"JWT Phone: {jwt_phone}")
