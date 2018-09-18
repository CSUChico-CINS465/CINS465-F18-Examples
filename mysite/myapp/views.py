from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"title":"Awesome"}
    return render(request, "index.html",context=context)

def page(request, num, year):
    context = {
        "title":"Awesome",
        "page":num
        }
    return render(request, "index.html",context=context)
