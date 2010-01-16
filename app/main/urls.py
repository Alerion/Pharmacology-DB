from django.conf.urls.defaults import *

urlpatterns = patterns('app.main.views',
    url(r'^$', 'index', name='index'),
    url(r'^urls.js$', 'urls', name='urls'),
    url(r'^drug_edit_cm.js$', 'drug_edit_cm', name='drug_edit_cm'),
    url(r'^dice/$', 'dice', name='dice'),
    url(r'^drugs_tree/$', 'drugs_tree', name='drugs_tree'),
    url(r'^load_drug_grid/$', 'load_drug_grid', name='load_drug_grid'),
    url(r'^drug_info/$', 'drug_info', name='drug_info'),
    url(r'^save_drug_value/$', 'save_drug_value', name='save_drug_value'),
    url(r'^select/$', 'select', name='select'),
)