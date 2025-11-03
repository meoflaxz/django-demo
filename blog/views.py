from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    """Display all posts"""
    posts = Post.objects.all()
    # create variable all post in dictionary named context
    context = {'post': posts}
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    """Display single post"""
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_details.html', context)


