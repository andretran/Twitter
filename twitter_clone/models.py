from django.db import models



class Tweet(models.Model):
    author = models.ForeignKey('User')
    text = models.CharField(max_length = 140)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.author.name + " - " + self.text

class Follow(models.Model):
    follower = models.ForeignKey('User')
    followee = models.ForeignKey('User', related_name = 'followee')

class User(models.Model):
    name = models.CharField(max_length = 20)
    following = models.ManyToManyField('self', through='Follow', related_name = 'follower', symmetrical=False)
    # tweets = models.ForeignKey('Tweet')
    def __str__(self):
        return self.name
