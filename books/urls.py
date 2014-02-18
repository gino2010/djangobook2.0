from django.conf.urls import patterns, url
from books import views

__author__ = 'Gino'

urlpatterns = patterns('',
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search, name='search'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
)