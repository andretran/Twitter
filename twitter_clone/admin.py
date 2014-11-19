from django.contrib import admin
from twitter_clone.models import Tweet, Follow, User


admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Follow)
# Register your models here.
