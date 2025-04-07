from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
