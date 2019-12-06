from django.urls import path
from .views import add_comment, blog_post

urlpatterns = [
  path('add/<int:post_id>/', add_comment, name="add_comment"),
  path('get', blog_post, name="get_comment")
]