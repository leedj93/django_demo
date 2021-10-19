from django.shortcuts import render

# Create your views here.
def local_shops(request):
    return render(request, "local/shops.html")
