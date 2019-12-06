from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Comment, Post
from .forms import CommentForm
from .serializers import CommentSerializer
import pytz

# Django Rest Framework for seeing the JSON
@api_view(['POST'])
def add_comment(request, post_id):

  # Create a form instance and populate it with data from the request:
  form = CommentForm(request.POST)

  comment_data = dict(request.data)
  comment_data['_post'] = Post.objects.filter(id=post_id)[:1].get()

  if form.is_valid():
    # Make a serializer with the JSON from the request
    serializer = CommentSerializer(data=comment_data)
    # Checks that the JSON has the right fields
    import pdb
    pdb.set_trace()
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

  return redirect('/posts/{}/'.format(post_id))

# Display the comments / post
def blog_post(request, post_id):
  # Post
  post = Post.objects.filter(id=post_id)[:1].get()

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
  db_comments = Comment.objects.filter(_post=post_id)
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
                template_name="posts.html", 
                context={
                  'comments': comments, 
                  'post': post, 
                  'errors': form_errors.values(),
                  'form': form, 
                  'post_id': post_id, 
                  'num_comments': len(comments)
                })


# List the posts
def index(request):
  # Post
  posts = Post.objects.all()
  print(posts)    
  # Render the html for the post
  return render(request, 
                template_name="index.html", 
                context={
                  'posts': posts
                })