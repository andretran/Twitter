from django.conf.urls import url
from twitter_clone import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
