from lib import render_to
from django.core.urlresolvers import reverse

@render_to('main/index.html')
def index(request):
    return {}

@render_to('main/urls.js')
def urls(request):
    from urls import urlpatterns
    output = []
    for item in urlpatterns:
        output.append((item.name, reverse('main:'+item.name)))
    
    return {
        'urls': output 
    }