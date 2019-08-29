from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from .models import Profile
from .forms import ProfileForm

# Create your views here.

def main(request):
    return render(request, 'account/main.html')
def signup(request):
    if request.user.is_authenticated:
        return redirect('list', user_id=request.user.id)
    if request.method=='POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error1': '이미 사용 중인 아이디입니다.'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                profile = Profile.objects.create(user=user)
            auth.login(request, user)
            return redirect('list', user_id=request.user.id)
        else:
            return render(request, 'account/signup.html', {'error2': '비밀번호가 일치하지 않습니다.'})
    else:
        # User watns to enter info
        return render(request, 'account/signup.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('list', user_id=request.user.id)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('list', user_id=request.user.id)
        else:
            return render(request, 'account/login.html', {'error': '아이디나 비밀번호가 올바르지 않습니다.'})
    else:
        return render(request, 'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def setting(request):
    form = ProfileForm()
    return render(request, 'account/setting.html', {'form': form})

def changepropic(request):
    if request.method=='POST':
        profile = request.user.profile
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('setting')
        else:
            img_error = '에러!'
            return render(request, 'account/settings.html', {'img_error': img_error})
        return redirect('setting')
    else:
        return redirect('list', user_id=request.user.id)

def changepassword(request):
    if request.method=='POST':
        user = request.user
        current_password = request.POST['current_password']
        if check_password(current_password, user.password):
            if request.POST['password1'] == request.POST['password2']:
                new_password = request.POST['password1']
                user.set_password(new_password)
                user.save()
                auth.login(request, user)
                return redirect('list', user_id=request.user.id)
            else:
                error = '비밀번호가 일치하지 않습니다.'
        else:
            error = '현재 비밀번호가 일치하지 않습니다.'
    else:
        return redirect('list', user_id=request.user.id)
    return render(request, 'account/setting.html', {'error': error})