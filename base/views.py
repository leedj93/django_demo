from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "weather": "맑음",
        "temp": "30도",
    }
    return render(request, "index.html", context)
