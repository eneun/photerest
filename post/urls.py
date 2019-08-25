from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:user_id>', views.listing, name='list'),
    path('show/<int:post_id>', views.show, name='show'),
    path('new/', views.new, name='new'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('postdelete/<int:post_id>', views.postdelete, name='postdelete'),
]