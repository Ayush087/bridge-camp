from django.shortcuts import render, HttpResponse

# Create your views here.


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")


def index(request):
    context = {
        "var1": "Ayush Baranwal",
        "var2": "Bhatpar Rani"
    }
    return render(request, "index.html", context)
