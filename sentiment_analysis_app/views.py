from django.shortcuts import render
# from . import utils
from .analysis import analysis as a


def index(request):
    if "submit-button" in request.POST:
        user_input = request.POST.get("param")
        result = a.calculating(str(user_input))
        sentence = "The sentiment is "
        return render(request, "index.html",{"result": result, "sentence": sentence})
    
    return render(request, "index.html")

def yelp(request):
    chart_df = a.yelp()
    chart, df = chart_df
    print(df)
    
    return render(request, "yelp.html", {"chart": chart})