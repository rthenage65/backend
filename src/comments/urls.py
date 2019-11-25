from django.urls import path
from .views import add_comment, blog_post

urlpatterns = [
  path('add', add_comment, name="add_comment"),
  path('get', blog_post, name="get_comment")
]