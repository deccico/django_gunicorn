from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^classes/$', 'classes.views.index'),
    url(r'^classes/(?P<class_id>\d+)/$', 'classes.views.detail'),
    url(r'^classes/(?P<class_id>\d+)/results/$', 'classes.views.results'),
    url(r'^classes/(?P<class_id>\d+)/vote/$', 'classes.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)
