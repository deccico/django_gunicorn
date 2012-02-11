from django.conf.urls.defaults import patterns
from django.views.generic.simple import direct_to_template
 
urlpatterns = patterns('',
(r'^test_static/$',             direct_to_template, {'template': 'test_static.html'}),
)