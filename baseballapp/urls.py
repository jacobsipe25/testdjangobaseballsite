from django.contrib import admin
from django.urls import path,include
from baseballapp import views
from django.contrib.auth import views as auth
from django.conf.urls import url
from baseballapp.models import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path(r'login/',auth.login,name="login"),
    path(r"logout/",auth.logout,name="logout"),
    path(r'theplayers/',views.PlayerList,name="player_list"),
    url(r'^player/new',views.PlayerUpload,name="player_create"),
    url(r'player/(?P<pk>\d+)/$',views.PlayerDetail.as_view(),name="player_detail"),
    url(r'edit/(?P<pk>\d+)/$',views.PlayerUpdateView.as_view(),name="player_edit"),
    url(r'^player/delete/(?P<pk>\d+)/$',views.PlayerDeleteView.as_view(),name="delete"),
    url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    url(r'team/(?P<pk>\d+)/$',views.TeamDetail.as_view(),name="team_detail"),
    url(r'^team/new',views.TeamUpload,name="team_create"),
    url(r'^theteams/',views.TeamList,name="team_list"),


]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT )
