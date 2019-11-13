from django.urls import path
from .views import add_comment

urlpatters = [
    path('add', add_comment, name="add_comment")
]