from django.shortcuts import render
from django.http import JsonResponse
import requests

# Phone.email API credentials
CLIENT_ID = "YOUR_CLIENT_ID"
REDIRECT_URL = "YOUR_REDIRECT_URL"
AUTH_URL = f"https://auth.phone.email/log-in?client_id={CLIENT_ID}&redirect_url={REDIRECT_URL}"

def index(request):
    try:
        # Retrieve access_token from the query parameters
        access_token = request.GET.get('access_token', None)
        
        # Initialize user_details dictionary
        user_details = {'countryCode': '', 'phoneNo': '', 'jwt': ''}
        
        # Check if access_token is present
        has_token = access_token is not None
        
        # Data dictionary to be passed to the template
        data = {'hasToken': has_token, 'userDetails': user_details, 'authUrl': AUTH_URL}

        if has_token:
            # Fetch user details using the Phone.email API
            url = "https://eapi.phone.email/getuser"
            payload = {'access_token': access_token, 'client_id': CLIENT_ID}
            
            # Make a POST request to the Phone.email API
            response = requests.post(url, data=payload)
            
            # Parse the JSON response
            response_data = response.json()

            # Update user_details with fetched data
            user_details['countryCode'] = response_data['country_code']
            user_details['phoneNo'] = response_data['phone_no']
            user_details['jwt'] = response_data['ph_email_jwt']

        # Render the 'index.html' template with the data
        response = render(request, 'index.html', data)
        
        # Set the Cross-Origin-Opener-Policy header for handling popups
        response['Cross-Origin-Opener-Policy'] = 'same-origin-allow-popups' 

        return response

    except Exception as error:
        # Return a JSON response for internal server error
        return JsonResponse({'message': 'Internal server error.'}, status=500)
