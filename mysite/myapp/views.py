from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import logout
# from django.conf import settings
from django.contrib.auth.decorators import login_required

# import json

from . import models
from . import forms
# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_instance = forms.SuggestionForm(request.POST)
        if form_instance.is_valid():
            if request.user.is_authenticated:
                suggest = models.SuggestionModel(
                    suggestion=form_instance.cleaned_data["suggestion"],
                    author=request.user
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

@login_required
def comment(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_instance = forms.CommentForm(request.POST)
        if form_instance.is_valid():
            if request.user.is_authenticated:
                comment = models.CommentModel(
                    comment=form_instance.cleaned_data["comment"],
                    author=request.user
                )
                comment.save()
                form_instance = forms.CommentForm()
    else:
        form_instance = forms.CommentForm()
    context = {
        "title":"Awesome",
        "form_instance":form_instance
        }
    return render(request, "comment.html", context=context)

def page(request, num, year):
    context = {
        "title":"Awesome",
        "page":num
        }
    return render(request, "index.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/login/")

def register(request):
    if request.method == 'POST':
        registration_form = forms.RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save(commit=True)
            return redirect("/")
    else:
        registration_form = forms.RegistrationForm()
    context = {
        "form":registration_form
        }
    return render(request, "registration/register.html", context=context)

def rest_suggestion(request):
    if not request.user.is_authenticated:
        return JsonResponse({"suggestions":[]})
    if request.method == 'GET':
        suggestions = models.SuggestionModel.objects.all()
        list_of_suggestions = []
        for suggest in suggestions:
            list_of_suggestions += [{
                "suggestion":suggest.suggestion,
                "author":suggest.author.username,
                "id":suggest.id
            }]
        return JsonResponse({"suggestions":list_of_suggestions})
    return HttpResponse("Invalid HTTP Method")
