from django.shortcuts import render
from django.contrib.auth.models import User
from post.models import Post
from labeling.models import Category

# Create your views here.
def recommend(request):
    from itertools import chain
    from django.contrib.postgres.fields import ArrayField
    from finding.models import Interest

    # 내 관심사
    interests = Interest.objects.filter(user=request.user)

    # 내 관심사를 가진 다른 사용자
    users = find_others_by_interest(request.user)


    # recomment.html에서 특정 카테고리로 검색한 글 보여주기
    # posts = Post.objects.exclude(user=request.user).order_by('user').values('id')
    # cats = Category.objects.filter(category=interests[0]).values('post')
    # results = posts.intersection(cats)
    # # print(posts)
    # # print(cats)
    # results = list(results)
    # id_list = []
    # for result in results:
    #     id_list.append(result['id'])
    # print(id_list)



    # for post in posts:
    #     print(post.category_set.all())

    # 트렌드 : 카테고리 db에서 가장 많은 순서대로 세기
    # result = Category.objects.values('category').order_by('category').annotate(count=Count('category'))
    # print(result)

    # pst = Post.objects.annotate(Count('category_set'))
    # # print(pst)
    # pst = pst.values_list('content', 'category_set__count')
    # print(pst)

    # categoris = Category.objects.annotate(Count('category'))
    # categoris = categoris.values_list('category', 'category__count')
    # pst = Post.objects.exclude(user=request.user)
    # for category in categoris:
    #     # if category[0].post.user != request.user:
    #     print(category)
    # # print(pst)

    
    
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
        users = User.objects.filter(interest__interest=interests[0]).exclude(id=user.id)
    elif len(interests) == 2:
        users = User.objects.filter(interest__interest=interests[0]) | User.objects.filter(interest__interest=interests[1])
        users = users.exclude(id=user.id)
    elif len(interests) == 3:
        users = User.objects.filter(interest__interest=interests[0]) | User.objects.filter(interest__interest=interests[1]) | User.objects.filter(interest__interest=interests[2])
        users = users.exclude(id=user.id)
    return users