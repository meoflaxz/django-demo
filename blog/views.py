from django.shortcuts import render
from .models import Post

def post_list(request):
    """Display all posts"""
    posts = Post.objects.all()
    context = {'post': posts}
    return render(request, 'blog/post_list.html', context)


