from django.conf.urls import patterns, url
from others import views
from others.views import temp_home, ordering, navtemp, my_image, unruly_passengers_csv, hello_pdf, LatestEntries

__author__ = 'Gino'

urlpatterns = patterns('',
    url(r'^$', temp_home),
    url(r'^image/$', my_image),
    url(r'^ordering/$', ordering),
    url(r'^(?P<title>[^/]+)/(?P<current>\d+)/$', navtemp),
    # chapter08
    url(r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
    url(r'^bar/$', views.foobar_view, {'template_name': 'template2.html'}),
    url(r'^mydata/birthday/$', views.my_view, {'month': 'jan', 'day': '06'}),
    url(r'^mydata/(?P<month>\w{3})/(?P<day>\d\d)/$', views.my_view),
    url(r'^mydata/(\d{4})/(\d{2})/(\d{2})/$', views.day_archive),
    url(r'^filter/$', views.filter_view),

    #chapter13
    url(r'^cvs/$', unruly_passengers_csv),
    url(r'^hello_pdf/$', hello_pdf),
    url(r'^feeds/latest/$', LatestEntries()),
    url(r'^feeds/latest/$', LatestEntries()),
    url(r'^atoms/latest/$', LatestEntries()),
    url(r'^test/(?P<url>.*)$', views.test_len),

    #chapter14
    url(r'^set_cookies/$', views.set_color),
    url(r'^show_cookies/$', views.show_color),

    url(r'^set_session/$', views.set_color_session),
    url(r'^show_session/$', views.show_color_session),

    url(r'^test_cookies/$', views.test_cookies, name='test'),

)