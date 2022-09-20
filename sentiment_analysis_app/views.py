from django.shortcuts import render
from .analysis import analysis as a

def index(request):
    if "submit-button" in request.POST:
        user_input = str(request.POST.get("entered"))
        
        #minimum charcter limit BERT
        if len(user_input) < 3:
            return render(request, "index.html", {"error": "Please enter atleast 3 characters!"})
        
        result = a.calculating(user_input)
        sentence = "The sentiment is "
        return render(request, "index.html",{"result": result, "sentence": sentence})
    
    return render(request, "index.html")


def yelp(request):
    if "yelp-submit-button" in request.POST:
        user_input = str(request.POST.get("url"))

        check_1 = "https://www.yelp."
        check_2 = "www.yelp.ie"

        if user_input[:17] != check_1 or user_input == check_2:
            return render(request, "yelp.html", {"error": "Invalid URL"})
        
        result = a.yelp(user_input)
        chart, reviews, sentiments = result
        
        if request.POST.get("table-option", "") == "on":
            return render(request, "yelp.html", {"chart": chart, "reviews": reviews, "sentiments": sentiments, "table": " "})
        
        return render(request, "yelp.html", {"chart": chart, "reviews": reviews, "sentiments": sentiments, "no_table": " "})
    
    return render(request, "yelp.html")