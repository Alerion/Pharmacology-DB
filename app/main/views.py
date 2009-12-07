from lib import render_to, ajax_processor
from django.core.urlresolvers import reverse
from models import ATCCategory, Drug, CompareValue, CRITERION_CHOICE

@render_to('main/index.html')
def index(request):
    return {
        'criterions': CRITERION_CHOICE
    }

@render_to('main/drug_info.html')
def drug_info(request):
    return {
        'item': Drug.objects.get(pk=request.POST['pk'])    
    }

@ajax_processor
def save_drug_value(request):
    post = request.POST
    obj = CompareValue.set_value(criterion=int(post['criterion']), 
                              left=int(post['left']), 
                              top=int(post['top']),
                              value=int(post['value']))
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

@render_to('main/drug_edit_cm.js')
def drug_edit_cm(request):
    return {
        'items': Drug.objects.all()
    }

@ajax_processor
def drugs_tree(request):
    items = ATCCategory.objects.all()
    return [item.tree_node() for item in items]

@ajax_processor
def load_drug_grid(request):
    output = []
    pk = int(request.POST['pk'])
    pks = map(int, request.POST.getlist('pks'))
    for item in CRITERION_CHOICE:
        output.append(CompareValue.grit_row(item, pk, pks))
    return {'items': output} 
    
def dice(request):
    from django.http import HttpResponse
    from random import shuffle
    input = [1, 2, 3, 4, 5, 6]
    r = []
    for i in range(3):
        shuffle(input)
        r.append(input[0])
        input = [1, 2, 3, 4, 5, 6]
    r.append(sum(r))
    return HttpResponse('<div style="margin: 200px; font-size: 2em;">%s  %s  %s  =  %s</div>' % tuple(r))