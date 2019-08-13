from django.shortcuts import render, get_object_or_404
from post.models import Post

# Create your views here.
def list(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'post/list.html', {'posts': posts})

def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/show.html', {'post': post})