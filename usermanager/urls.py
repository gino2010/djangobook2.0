from django.conf.urls import patterns, url
from usermanager import views

__author__ = 'Gino'

urlpatterns = patterns('',
    url(r'^$', views.user_home),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
)