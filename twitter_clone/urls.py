from django.conf.urls import url
from twitter_clone import views

from twitter_clone.models import User, Tweet, Follow

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^/tweets/$', views.tweets, name='tweets')
]
