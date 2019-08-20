from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from post.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.
def commentcreate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('show', post_id=post.pk)
        else:
            return redirect('show', post_id=post.pk)
    else:
        form = CommentForm()
        return redirect('show', post_id=post.pk)

def commentdelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('show', post_id=comment.post.pk)