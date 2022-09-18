from django.shortcuts import render
from .analysis import analysis as a

def index(request):
    if "submit-button" in request.POST:
        user_input = request.POST.get("entered")
        result = a.calculating(str(user_input))
        sentence = "The sentiment is "
        return render(request, "index.html",{"result": result, "sentence": sentence})
    
    return render(request, "index.html")

def yelp(request):
    if "yelp-submit-button" in request.POST:
        user_input = str(request.POST.get("url"))

        check_1 = "https://www.yelp." #[:17]
        check_2 = "www.yelp." #[:9]

        if user_input[:17] != check_1 and user_input != check_2:
            return render(request, "yelp.html", {"error": "Invalid URL"})
        
        chart_df = a.yelp()
        chart, df = chart_df
        print(df)
        
        return render(request, "yelp.html", {"chart": chart})
    
    return render(request, "yelp.html")