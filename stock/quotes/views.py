from django.shortcuts import render

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_3321d966bf1d440bb0289ace9cab26f1")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "ERROR..."
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol"})

    

def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
     return render(request, 'add_stock.html', {})
