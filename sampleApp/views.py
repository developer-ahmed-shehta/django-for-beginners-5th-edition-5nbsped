from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):

    return HttpResponse("Hello, world. You're at the polls home view.")

def about(request):
    context = {
        "name": "Shehta",
        "age": 25
    }
    return render(request,"sampleApp/about.html",context)