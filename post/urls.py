from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('show/<int:post_id>', views.show, name='show'),
]
