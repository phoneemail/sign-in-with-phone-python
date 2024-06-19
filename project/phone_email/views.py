from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

def dashboard(request):
    # Render the dashboard page
    
    response = render(request, 'home.html')
    # Set the Cross-Origin-Opener-Policy header for handling popups
    response['Cross-Origin-Opener-Policy'] = 'same-origin-allow-popups'
    return response
    
    # return render(request, 'sign_in.html')