from django.http import HttpResponse
from django.template import RequestContext, loader
import simplejson
import debugger
# from django.core import serializers
from twitter_clone.models import User, Tweet, Follow
from django.views.decorators.csrf import csrf_exempt

def index(request):
    users = User.objects.all()
    template = loader.get_template('twitter_clone/index.html')
    context = RequestContext(request, {
        'users': users
    })
    return HttpResponse(template.render(context))

@csrf_exempt
def create(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id = user_id)
        tweet = request.POST.get('tweet')
        new_tweet = Tweet(text = tweet, author = user)
        new_tweet.save()
        response = {'text': new_tweet.text, 'author': new_tweet.author.name, 'time': new_tweet.time.strftime('%a. %d, %Y, %I %p')}
        json = simplejson.dumps(response)
        return HttpResponse(json)

def show(request, user_id):
    profile = User.objects.get(id = user_id)
    tweets = profile.get_tweets
    template = loader.get_template('twitter_clone/show.html')
    context = RequestContext(request, { 'profile' : profile, 'tweets' : tweets})
    return HttpResponse(template.render(context))
