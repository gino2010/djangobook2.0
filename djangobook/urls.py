from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
#chapter03
# from djangobook.views import hello, my_homepage_view, current_datetime, hours_ahead, display_meta
# chapter08 better way
from djangobook import views

# -----------another way----------
# from django.conf.urls.defaults import *
# urlpatterns = patterns('djangobook.views',
#     (r'^hello/$', 'hello'),
#     (r'^time/$', 'current_datetime'),
#     (r'^time/plus/(d{1,2})/$', 'hours_ahead'),
# )
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangobook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #chapter03
    url(r'^$', views.my_homepage_view),
    url(r'^hello/$', views.hello),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),

    #chapter04
    url(r'^temp/', include('temp.urls')),

    #chapter06
    url(r'^admin/', include(admin.site.urls)),

    #chapter07
    url(r'^meta/$', views.display_meta),
    url(r'^books/', include('books.urls', namespace='books'))
)

# chapter08 debug url patterns
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^debuginfo/$', views.debug),
    )