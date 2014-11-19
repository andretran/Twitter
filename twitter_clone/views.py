from django.http import HttpResponse
from django.template import RequestContext, loader
# from django.utils import simplejson
# from django.core import serializers
from twitter_clone.models import User, Tweet, Follow


def index(request):
    tweets = Tweet.objects.all()
    template = loader.get_template('twitter_clone/index.html')
    context = RequestContext(request, {
        'tweets': tweets
    })
    return HttpResponse(template.render(context))
    # following = User.objects.get(id = 1).following.all().tweets
    # tweets = []
    # for user in following:
    #     for tweets in
    # json_data = simplejson.dumps({'tweets':tweets})
    # return HttpResponse(json_data,  mimetype='application/json')



# def tweets(request):
#     tweets = User.objects.get(id = 1).following.all()
#     return json.dumps(tweets)
# Create your views here.
