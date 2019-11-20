from django.urls import path
from .views import blog_post

urlpatterns = [
    path('get', blog_post, name="get-comment"),
]