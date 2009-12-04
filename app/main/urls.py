from django.conf.urls.defaults import *

urlpatterns = patterns('app.main.views',
    url(r'^$', 'index', name='index'),
    url(r'^urls.js$', 'urls', name='urls')
)