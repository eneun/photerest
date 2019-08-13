from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from post.models import Post
from .forms import PostForm
from follow.models import Follow

# Create your views here.
def list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(user=user_id)
    follow = Follow.objects.filter(send=request.user, receive=user)
    return render(request, 'post/list.html', {'posts': posts, 'user': user ,'follow': follow})

def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/show.html', {'post': post})

def new(request):
    return render(request, 'post/new.html')

def postcreate(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('list', user_id=request.user.id)
        else:
            return redirect('list')
    else:
        form = PostForm()
        return render(request, 'post/new.html', {'form': form})

def postdelete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('list', user_id=request.user.id)