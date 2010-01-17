from lib import render_to, ajax_processor
from django.core.urlresolvers import reverse
from models import FarmAction, Drug, CompareValue, CRITERION_CHOICE
from django.http import HttpResponse
from criterion import criterion
from lib.mai import Matrix, MAI

@render_to('main/index.html')
def index(request):
    return {
        'group_pk': request.GET.get('pk', 1),
        'criterions': CRITERION_CHOICE
    }

def select(request):
    qs = Drug.objects.all()
    mai = MAI(criterion.get_matrix())
    pks = [item.pk for item in qs]
    for cr in criterion.iter():
        alternative = Matrix()
        for drug in qs:
            alternative.append(CompareValue.matrix_row(cr, drug.pk, pks))
        mai.add_alter(alternative)
    result = [item for item in mai()]
    for i in range(len(result)):
        print '%s - %s' % (qs[i].pk, result[i])    
    return HttpResponse('Text!')

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
                              value=post['value'])
    return {}

@render_to('main/urls.js')
def urls(request):
    from urls import urlpatterns
    output = []
    for item in urlpatterns:
        output.append((item.name, reverse('main:'+item.name)))
    
    return {
        'group_pk': request.GET.get('pk', 1),
        'urls': output 
    }

@render_to('main/drug_edit_cm.js')
def drug_edit_cm(request):
    pk = request.GET.get('pk', 1)
    return {
        'items': Drug.objects.filter(category=pk)
    }

@ajax_processor
def farmaction_tree(request):
    return [item.farm_tree_node() for item in FarmAction.objects.all()]    

@ajax_processor
def drugs_tree(request):
    pk = request.GET.get('pk', 1)
    item = FarmAction.objects.get(pk=pk)
    return [item.tree_node()]

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