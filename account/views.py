from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method=='POST':
        # User has info and wants an accunt now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error1': '이미 사용 중인 아이디입니다.'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'account/signup.html', {'error2': '비밀번호가 일치하지 않습니다.'})
    else:
        # User watns to enter info
        return render(request, 'account/signup.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'account/login.html', {'error': '아이디나 비밀번호가 올바르지 않습니다.'})
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return render(request, 'account/signup.html')