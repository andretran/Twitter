from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^twitter/', include('twitter_clone.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
