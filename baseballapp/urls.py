from django.contrib import admin
from django.urls import path,include
from baseballapp import views
from django.contrib.auth import views as auth
from django.conf.urls import url
from baseballapp.models import Player
urlpatterns = [
    path(r'login/',auth.login,name="login"),
    path(r"logout/",auth.logout,name="logout"),
    path(r'theplayers/',views.PlayerList.as_view(),name="player_list"),
    url(r'^player/new',views.CreatePlayer.as_view(),name="player_create"),
    url(r'player/(?P<pk>\d+)/$',views.PlayerDetail.as_view(),name="player_detail"),
    url(r'edit/(?P<pk>\d+)/$',views.PlayerUpdateView.as_view(),name="player_edit"),
    url(r'^player/delete/(?P<pk>\d+)/$',views.PlayerDeleteView.as_view(),name="delete"),
    url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),

]
