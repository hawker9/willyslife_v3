from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests



# Create your views here.
def index(request):
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPXL&outputsize=full&apikey=8DI2YTBO8A4SZ5BR&datatype=json')
    print(r.text)
    return HttpResponse('<pre><b>'"<a href=https://willyslife.herokuapp.com/db/>Other Page</a><p style=font-size:48px>&#128151Wills website!&#128151</b></p><br><br>Below is an API to the stock data for SPXL ticker:" +'<br><br><br>'+ r.text +  '</pre>')


def db(request):
    return HttpResponse('<pre><b><p style=font-size:48px>&#128293&#128293&#128293&#128293</b></p><br><br>Page # 2 of Willy</pre>')





"""greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})"""


