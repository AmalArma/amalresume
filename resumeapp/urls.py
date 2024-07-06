
from django.urls import path
from .import views

urlpatterns = [

    path('',views.index,name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('resume', views.resume, name='resume'),
    path('send/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),

]
