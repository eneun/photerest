from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('setting/', views.setting, name='setting'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('changepropic/', views.changepropic, name='changepropic'),
]