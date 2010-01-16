# -*- coding: utf-8 -*-
from lib.mai import Matrix, MAI
from django.utils import simplejson as json

class Criterion(object):
    
    CHOICE = (
        (1, u'Эфективность'),
        (2, u'Цена'),
        (3, u'Доступность'),
        (4, u'Фармдействие')
    )
    
    def __init__(self):
        self._items = []
        m = Matrix()
        m.append([1, 3, 3, 1/2.])
        m.append([1/3., 1, 2, 1/2.])
        m.append([1/3., 1/2., 1, 1/4.])
        m.append([2, 2, 4, 1])
        self._items.append({
            'name': u'Test1',
            'matrix': m,
            'default': True
        })
        m = Matrix()
        m.append([1, 1, 9, 9])
        m.append([1, 1, 9, 9])
        m.append([1/9., 1/9., 1, 1])
        m.append([1/9., 1/9., 1, 1])
        self._items.append({
            'name': u'Test2',
            'matrix': m,
            'default': False
        })
        m = Matrix()
        m.append([1, 1, 1, 1])
        m.append([1, 1, 1, 1])
        m.append([1, 1, 1, 1])
        m.append([1, 1, 1, 1])
        self._items.append({
            'name': u'Test3',
            'matrix': m,
            'default': False
        })
        
    def get_matrix(self, type=None):
        if type:
            return self._items[type]['matrix']
        else:
            for item in self._items:
                if item['default']:
                    return item['matrix']
    
    def _get_info(self, m):
        w = m._w
        info = []
        for i in range(len(w)):
            info.append('%s: %s' % (self.CHOICE[i][1], round(w[i], 2)))
        return '<br/>'.join(info) 
                   
    def get_matrix_choices_json(self):
        output = []
        for i in range(len(self._items)):
            item = self._items[i]
            el = {
                'text': item['name'],
                'group': 'matrix',
                'pk': i,
                'checked': item ['default'],
                'info': self._get_info(item['matrix'])
            }
            output.append(el)
        return json.dumps(output)

    def get_matrix_choices(self):
        output = []
        for i in range(len(self._items)):
            item = self._items[i]
            output.append((i, item['name']))
        return output
    
    def iter(self):
        for item in self.CHOICE:
            yield item
    
criterion = Criterion()

CRITERION_CHOICE = criterion.CHOICE    