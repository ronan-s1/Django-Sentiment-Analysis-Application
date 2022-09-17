from django.shortcuts import render
from . import utils


def index(request):
    return render(request, "index.html")

def result(request): 
    user_input = request.POST.get("param")
    result = utils.calculating(str(user_input))
    sentence = "The sentiment is "
    return render(request, "index.html",{"result": result, "sentence": sentence})

def yelp(request):
    uri = utils.yelp()
    return render(request, "yelp.html", {"chart": uri})