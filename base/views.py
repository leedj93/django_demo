from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "weather": "맑음",
        "temp": "30도",
    }
    return render(request, "index.html", context)

def base_ih(request):
    context = {
        "weather": "맑음",
        "temp": "30도",
    }
    return render(request, "base_IH.html", context)

def test_1(request):
    return render(request, "test_1.html")

def test_2(request):
    return render(request, "test_2.html")

def test_3(request):
    return render(request, "test_3.html")
