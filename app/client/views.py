from lib import render_to, ajax_processor
from django.core.urlresolvers import reverse
from app.main.models import Illness, FarmAction
from app.main.criterion import criterion
from forms import SearchForm

@render_to('client/index.html')
def index(request):
    return {
        'criterions': criterion.get_matrix_choices_json()
    }

@ajax_processor
def farm_tree(request):
    return [item.client_farm_tree_node() for item in FarmAction.objects.all()]     

@ajax_processor
def illness_tree(request):
    items = Illness.objects.all()
    return [item.tree_node() for item in items]

@render_to('client/urls.js')
def urls(request):
    from urls import urlpatterns
    output = []
    for item in urlpatterns:
        output.append((item.name, reverse('client:'+item.name)))
    
    return {
        'urls': output 
    }

@ajax_processor
def search(request):
    output = {
         'success': False,
         'items': []     
    }
    form = SearchForm(request.POST)
    if form.is_valid():
        result = form.search()
        for item in result:
            el = {
                'pk': item['item'].pk,
                'name': item['item'].name,
                'value': item['value']
            }
            output['items'].append(el)
        output['success'] = True
    return output