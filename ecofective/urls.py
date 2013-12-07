from django.conf.urls import patterns, include, url
from polls.views import hello, current_datetime, hours_ahead

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecofective.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^$', current_datetime),
)
