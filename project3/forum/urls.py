from . import views
from django.urls import path, re_path

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('profile/password', views.modify_password, name='modify_password'),
    path('profile/email', views.modify_email, name='modify_email'),
    path('profile', views.modify_profile, name='modify_profile'),
    path('sections/add', views.add_section, name='add_section'),
    path('sections', views.sections, name='sections'),
    re_path('^topics/(?P<id>\d+)/add/$', views.add_topic, name='add_topic'),
    re_path('^topics/(?P<id>\d+)/$', views.topics, name='topics'),
    re_path('^posts/(?P<id>\d+)/add/$', views.add_post, name='add_post'),
    re_path('^posts/(?P<id>\d+)/delete/$', views.delete_topic, name='delete_topic'),
    re_path('^posts/(?P<id>\d+)/$', views.posts, name='posts'),
    re_path('^details/(?P<id>\d+)/modify/$', views.modify, name='modify'),
    re_path('^details/(?P<id>\d+)/delete/$', views.delete, name='delete'),
    re_path('^details/(?P<id>\d+)/$', views.details, name='details'),
    path('', views.login, name='login')
]