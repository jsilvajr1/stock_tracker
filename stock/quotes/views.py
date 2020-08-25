from django.shortcuts import render

def home(request):
    import requests
    import json

    # pk_3321d966bf1d440bb0289ace9cab26f1
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_3321d966bf1d440bb0289ace9cab26f1")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "ERROR..."

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})