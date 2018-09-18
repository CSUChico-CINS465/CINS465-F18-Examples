from django.shortcuts import render

from . import models
# Create your views here.

def index(request):
    suggestions = models.SuggestionModel.objects.all()
    context = {
        "title":"Awesome",
        "suggestions":suggestions
        }
    return render(request, "index.html", context=context)

def page(request, num, year):
    context = {
        "title":"Awesome",
        "page":num
        }
    return render(request, "index.html", context=context)
