from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# import json

from . import models
from . import forms
# Create your views here.

def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_instance = forms.SuggestionForm(request.POST)
        if form_instance.is_valid():
            suggest = models.SuggestionModel(
                suggestion=form_instance.cleaned_data["suggestion"]
            )
            suggest.save()
            form_instance = forms.SuggestionForm()
    else:
        form_instance = forms.SuggestionForm()
    suggestions = models.SuggestionModel.objects.all()
    context = {
        "title":"Awesome",
        "suggestions":suggestions,
        "form_instance":form_instance
        }
    return render(request, "index.html", context=context)

def page(request, num, year):
    context = {
        "title":"Awesome",
        "page":num
        }
    return render(request, "index.html", context=context)

def rest_suggestion(request):
    if request.method == 'GET':
        suggestions = models.SuggestionModel.objects.all()
        list_of_suggestions = []
        for suggest in suggestions:
            list_of_suggestions += [{
                "suggestion":suggest.suggestion,
                "id":suggest.id
            }]
        return JsonResponse({"suggestions":list_of_suggestions})
    else:
        return HttpResponse("Invalid HTTP Method")
