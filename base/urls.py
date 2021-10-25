from django.urls import path

from base import views

urlpatterns = [
    path("", views.index),
    path("inherit/", views.base_ih),
    path("test_1/", views.test_1),
    path("test_2/", views.test_2),
    path("test_3/", views.test_3),
]