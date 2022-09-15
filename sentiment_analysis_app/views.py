from django.shortcuts import render
# from subprocess import run, PIPE
from analysis import analysis

def index(request):
    return render(request, "index.html")


def result(request):
    user_input = request.POST.get("param")
    result = analysis.calculating(user_input)
    sentence = "The sentiment is "
    return render(request, "index.html",{"result": result, "sentence": sentence})
