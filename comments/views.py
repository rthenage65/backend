from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from django.shortcuts import redirect

# Displays comments
def blog_post(request):
    if request.POST:
        # Make a serializer with the JSON from the request
        serializer = CommentSerializer(data=request.POST)
        # Checks that the JSON has the right fields
        if serializer.is_valid():
            # Saves object to database
            serializer.save()
            return redirect('/')

    # Get comments
    comments = Comment.objects.all()
    # Render the html for the post
    return render(request,
                  template_name="index.html",
                  context={'comments': comments})