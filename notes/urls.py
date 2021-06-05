from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('notes', views.notes, name='notes'),
    path('queries', views.queries, name='queries'),
    path('viewnote/<int:myid>', views.viewnote, name='viewnote'),
    path('delet/<int:myid>', views.delet, name='delet'),
    ]
