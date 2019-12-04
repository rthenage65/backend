from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Comment, Post
from .forms import CommentForm
from .serializers import CommentSerializer
import pytz

# Django Rest Framework for seeing the JSON
@api_view(['POST'])
def add_comment(request):

  # Create a form instance and populate it with data from the request:
  form = CommentForm(request.POST)

  if form.is_valid():
    # Make a serializer with the JSON from the request
    serializer = CommentSerializer(data=request.data)
    # Checks that the JSON has the right fields
    if serializer.is_valid():
      # Saves the object to the database
      serializer.save()
  else:
    # Get the errors from the form
    errors = form.errors.as_data()
    comment_errors = {}
    for key, val in errors.items():
      # Convert the error to a string so it can be stored
      comment_errors[key] = val[0].messages
    # Cache the errors
    request.session["comment_errors"] = comment_errors

  return redirect('/')

# Display the comments / post
def blog_post(request):
  # Post
  post = Post.objects.filter(id=1)[:1].get()

  # Comments
  form = CommentForm()
  form_errors = {}
  try:
    # Get comment errors if any from cache
    form_errors = request.session["comment_errors"]
    # Clear comment errors
    request.session["comment_errors"] = {}
  except KeyError:
    pass

  # Get all the comments
  db_comments = Comment.objects.all()
  comments = []
  # Just send the day of the comment, not the time
  for comment in db_comments.reverse():
      comments.append({
        'name': comment.name,
        'comment': comment.comment,
        'created': comment.created.date()
      })
      
  # Render the html for the post
  return render(request, 
                template_name="index.html", 
                context={
                  'comments': comments, 
                  'post': post, 
                  'errors': form_errors.values(),
                  'form': form, 
                  'num_comments': len(comments)
                })