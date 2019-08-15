from django.shortcuts import render, redirect, get_object_or_404
from post.models import Post
from .models import Like

# Create your views here.
def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like = Like.objects.filter(user=request.user, post=post)
    if like:
        like.delete()
    else:
        Like.objects.create(user=request.user, post=post)
    return redirect('show', post_id=post.pk)