from django.shortcuts import render

def index(request):
    # Render the index page    
    response = render(request, 'index.html')
    # Set the Cross-Origin-Opener-Policy header for handling popups
    response['Cross-Origin-Opener-Policy'] = 'same-origin-allow-popups'
    return response
