from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from post.models import Post
from django.contrib.auth.models import User
from .models import Follow

# Create your views here.
def follow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    follow = Follow.objects.filter(send=request.user, receive=user)
    if follow:
        follow.delete()
        return redirect('list', user_id=user.id)
    else:
        Follow.objects.create(send=request.user, receive=user)
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return redirect('list', user_id=user.id)