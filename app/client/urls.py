from django.conf.urls.defaults import *

urlpatterns = patterns('app.client.views',
    url(r'^$', 'index', name='index'),
    url(r'^urls.js$', 'urls', name='urls'),
    url(r'^illness_tree/$', 'illness_tree', name='illness_tree'),
    url(r'^search/$', 'search', name='search')    
)