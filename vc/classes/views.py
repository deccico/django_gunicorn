from django.template import Context, loader
from classes.models import Class
from django.http import HttpResponse

def index(request):
    latest_class_list = Class.objects.all().order_by('-class_date')[:5]
    t = loader.get_template('classes/index.html')
    c = Context({
        'latest_class_list': latest_class_list,
    })
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)