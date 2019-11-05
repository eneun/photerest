from django.shortcuts import render
from labeling.models import Category

# Create your views here.
def trend(request):
    from django.db.models import Count
    from post.models import Post

    # 트렌드 : 카테고리 db에서 가장 많은 순서대로 세기
    trends = Category.objects.values('category').order_by('category').annotate(count=Count('category'))
    # print(trends)
    trends = list(trends)[:3]
    # print(trends[0]['category'])

    first = trends[0]['category']
    second = trends[1]['category']
    third = trends[2]['category']

    first_trend = Post.objects.filter(category_set__category=first)
    second_trend = Post.objects.filter(category_set__category=second)
    third_trend = Post.objects.filter(category_set__category=third)

    # 나중에 삭제
    second_trend = second_trend.filter(id__gt=109) & second_trend.filter(id__lt=140).order_by('-created_at')

    return render(request, 'trend.html', {'first': first, 'second': second, 'third': third, 'first_trend': first_trend, 'second_trend': second_trend, 'third_trend': third_trend})