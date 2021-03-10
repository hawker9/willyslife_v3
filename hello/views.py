from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests


# Create your views here.
def index(request):
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPXL&outputsize=full&apikey=8DI2YTBO8A4SZ5BR&datatype=csv')
    print(r.text)
    return HttpResponse('<pre><b>'"<p style=font-size:48px> Wills website!&#128151</b></p><br><br>Below is an API to the stcok data for SPXL ticker:" +'<br><br><br>'+ r.text +  '</pre>')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
