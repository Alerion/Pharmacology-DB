# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def matrix(m):
    l = len(m)
    one = '<span class="one">%s</span>'
    large = '<span class="large">%s</span>'
    smalle = '<span class="smalle">%s</span>'
    for i in range(l):
        for j in range(l):
            val = round(m[i][j], 2)
            if val == 1:
                str_val = one % str(val)
            elif val > 1:
                str_val = large % str(val)
            else:
                str_val = smalle % str(val)
            m[i][j] = str_val 
    s = '<pre>%s</pre>'
    m_str = str(m).replace('], ', '],\n')[1:-1]
    return mark_safe(s % m_str)

register.filter('matrix', matrix)

def vector(v):
    o = []
    for item in v:
        o.append(str(round(item, 2)))
    return o

register.filter('vector', vector)
        