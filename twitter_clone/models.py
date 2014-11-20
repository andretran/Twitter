from django.db import models



class Tweet(models.Model):
    author = models.ForeignKey('User')
    text = models.CharField(max_length = 140)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.author.name + " - " + self.text

class Follow(models.Model):
    follower = models.ForeignKey('User', related_name = 'follower')
    followee = models.ForeignKey('User', related_name = 'followee')

class User(models.Model):
    name = models.CharField(max_length = 20)
    # follows = models.ManyToManyField('Follow', through='')
    following = models.ManyToManyField('self', through='Follow', symmetrical=False)
    # tweets = models.ManyToManyField('Tweet', through='Follow', symmetrical=False)
    # tweets = models.ForeignKey('Tweet')

    def get_tweets(self):
        return Tweet.objects.filter(author__in = self.following.all()).order_by('-time') 

    def __str__(self):
        return self.name
