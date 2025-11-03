from django.shortcuts import render, get_object_or_404
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer

def post_list(request):
    """Display all posts"""
    posts = Post.objects.all()
    # create variable all post in dictionary named context
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    """Display single post"""
    # pk is unique post id
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)

@api_view(['GET'])
def api_post_list(request):
    """API endpoint to get all posts as JSON"""
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_post_detail(request, pk):
    """API endpoint to get single post as JSON"""
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    serializer = PostSerializer(post)
    return Response(serializer.data)

