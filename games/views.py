from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# This view handles the homepage listing all posts
def homepage(request):
    posts = BlogPost.objects.all().order_by('-created_at') # Gets newest posts first
    return render(request, 'games/index.html', {'posts': posts})

# This view handles opening a single blog post
def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'games/post_detail.html', {'post': post})

# Create your views here.
