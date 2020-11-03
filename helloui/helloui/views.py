from django.shortcuts import render
import requests

def getmsg(request):
    response = requests.get('http://localhost:8000/hello' )
    geodata = response.json()
    return render(request,'home.html', {
        'ip': '',
        'country': geodata
    })