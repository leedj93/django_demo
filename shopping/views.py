from django.shortcuts import render

# Create your views here.

def shopping_admin(request):
    return render(request, "shopping/admin.html")

def shopping_item(request):
    return render(request, "shopping/item.html")

def shopping_shop(request):
    return render(request, "shopping/shop.html")

