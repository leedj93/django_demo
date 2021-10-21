from django.urls import path

from blog import views

urlpatterns =[
    path("home/", views.blog_home),
    path("post/<int:post_id>/", views.blog_post),
    path("create/", views.blog_create),
    path("post-edit/<int:post_id>/", views.blog_edit),
    path("post-delete/<int:post_id>/", views.blog_delete),
]