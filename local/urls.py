from django.urls import path

from local import views

urlpatterns = [
    path("shops/", views.local_shops)
]