from django.conf.urls import patterns, url
from books import views
from books.models import Publisher
from django.views.generic.list import ListView

__author__ = 'Gino'

urlpatterns = patterns('',
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search, name='search'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^author/$', views.show_author, name='show_author'),
    # chapter11 Generic Views list_detail has been deprecated
    url(r'^publishers/$', ListView.as_view(queryset= Publisher.objects.all(),
                                           template_name='publisher_list_page.html',
                                           object)),
)