from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from post.models import Post
from comment.models import Comment
from .forms import PostForm
from comment.forms import CommentForm
from follow.models import Follow
from like.models import Like
from labeling.models import Label

# Create your views here.
def list(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(user=user_id)
    follow = Follow.objects.filter(send=request.user, receive=user)
    like_count=0
    for like in Like.objects.all():
        if like.post.user == user:
            like_count += 1
    return render(request, 'post/list.html', {'posts': posts, 'user': user ,'follow': follow, 'like_count': like_count})

def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like = Like.objects.filter(user=request.user, post=post)
    form = CommentForm()
    comments = Comment.objects.filter(post=post)
    return render(request, 'post/show.html', {'post': post, 'like': like, 'form': form, 'comments': comments})

def new(request):
    return render(request, 'post/new.html')

def postcreate(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            labeling(post)
            category(post)
            return redirect('list', user_id=request.user.id)
        else:
            return redirect('list')
    else:
        form = PostForm()
        return render(request, 'post/new.html', {'form': form})

def postdelete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # 하드코딩
    post.comment_set.all().delete()
    post.like_set.all().delete()
    post.label_set.all().delete()
    post.delete()
    return redirect('list', user_id=request.user.id)


def labeling(post):
    # export GOOGLE_APPLICATION_CREDENTIALS=/Users/ye/grad/apikey.json
    from google.cloud import vision
    from google.cloud.vision import types
    # 로컬 파일 오픈
    import io
    import os

    vision_client = vision.ImageAnnotatorClient()

    # 로컬 파일 오픈
    post.image.url
    file_name = os.path.join(
        os.path.dirname('/Users/ye/grad/photerest/media/'),
        post.image.name)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)

    # 이미지 주소 사용
    # uri= "https://sundial.csun.edu/wp-content/uploads/2017/05/dld.jpg"
    # image = vision.types.Image()
    # image.source.image_uri = uri

    response = vision_client.label_detection(image=image)
    labels = response.label_annotations
    
    for label in labels:
        # print(label.description)
        # label = Label.objects.create(label=label, post=post)
        l = Label()
        l.label = label.description
        l.post = post
        l.save()
    return

def category(post):
    from sklearn.externals import joblib
    from labeling.models import Category
    labels = Label.objects.filter(post=post)
    string = ''
    for label in labels:
        string = string + label.label + ' '
    
    clf_animal = joblib.load('/Users/ye/attemp/svm/svm_model/animal_clf.pkl')
    clf_game = joblib.load('/Users/ye/attemp/svm/svm_model/game_clf.pkl')
    clf_education = joblib.load('/Users/ye/attemp/svm/svm_model/education_clf.pkl')
    clf_travel = joblib.load('/Users/ye/attemp/svm/svm_model/travel_clf.pkl')
    clf_fitness = joblib.load('/Users/ye/attemp/svm/svm_model/fitness_clf.pkl')
    clf_technology = joblib.load('/Users/ye/attemp/svm/svm_model/technology_clf.pkl')
    clf_sports = joblib.load('/Users/ye/attemp/svm/svm_model/sports_clf.pkl')
    clf_food = joblib.load('/Users/ye/attemp/svm/svm_model/food_clf.pkl')
    clf_shopping = joblib.load('/Users/ye/attemp/svm/svm_model/shopping_clf.pkl')
    clf_face = joblib.load('/Users/ye/attemp/svm/svm_model/face_clf.pkl')
    clf_art = joblib.load('/Users/ye/attemp/svm/svm_model/art_clf.pkl')

    
    # print(clf_animal.predict([string]))
    if clf_animal.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='animal')
    if clf_game.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='game')
    if clf_education.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='education')
    if clf_travel.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='travel')
    if clf_fitness.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='fitness')
    if clf_technology.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='technology')
    if clf_sports.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='sports')
    if clf_food.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='food')
    if clf_shopping.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='shopping')
    if clf_face.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='face')
    if clf_art.predict([string]) == ['1']:
        category = Category.objects.create(post=post, category='art')
    
    