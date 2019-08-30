from django.shortcuts import render
from django.contrib.auth.models import User
from post.models import Post
from labeling.models import Category

# Create your views here.
def recommend(request):
    from itertools import chain
    # from django.contrib.postgres.fields import ArrayField
    from finding.models import Interest

    # 내 관심사
    interests = Interest.objects.filter(user=request.user)

    # 내 관심사를 가진 다른 사용자
    users = find_others_by_interest(request.user)

    
    return render(request, 'recommend.html', {'interests': interests, 'users': users})

def find_others_by_interest(user):
    from finding.models import Interest

    users = User.objects.exclude(id=user.id)[:3]
    interests = []
    for interest in Interest.objects.filter(user=user):
        interests.append(interest.interest)
    print(users)
    print(interests)
    if len(interests) == 1:
        users = User.objects.filter(interest__interest=interests[0]).exclude(id=user.id).distinct()
    elif len(interests) == 2:
        users = User.objects.filter(interest__interest=interests[0]) | User.objects.filter(interest__interest=interests[1])
        users = users.exclude(id=user.id).distinct()
    elif len(interests) == 3:
        users = User.objects.filter(interest__interest=interests[0]) | User.objects.filter(interest__interest=interests[1]) | User.objects.filter(interest__interest=interests[2])
        users = users.exclude(id=user.id).distinct()
    return users