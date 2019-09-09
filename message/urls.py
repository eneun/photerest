from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('', views.messages, name='messages'),
    path('show/<int:message_id>', views.show, name='show'),
    path('<int:user_id>/', views.messagecreate, name='messagecreate'),
]