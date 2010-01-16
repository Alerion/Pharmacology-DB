# -*- coding: utf-8 -*-
from django import forms
from app.main.criterion import criterion
from app.main.models import Illness, Drug, CompareValue
from lib.mai import Matrix, MAI

class SearchForm(forms.Form):
    type = forms.ChoiceField(choices=criterion.get_matrix_choices())
    strong = forms.BooleanField(required=False)
    illnesses = forms.ModelMultipleChoiceField(queryset=Illness.objects.all(), required=False)
    
    def search(self):
        cr_matrix = criterion.get_matrix(int(self.cleaned_data['type']))
        if not self.cleaned_data['illnesses']:
            return []
        qs = self._get_qs(self.cleaned_data['illnesses'], self.cleaned_data['strong'])
        pks = [item.pk for item in qs]
        if not pks:
            return []                
        mai = MAI(cr_matrix, qs)
        for cr in criterion.iter():
            alternative = Matrix()
            for drug in qs:
                alternative.append(CompareValue.matrix_row(cr, drug.pk, pks))
            mai.add_alter(alternative)
        return mai.sort() 
                
    def _get_qs(self, illnesses, strong):
        if strong:
            result = Drug.objects.all()
            for item in illnesses:
                result = result.filter(illnesses=item)
        else:
            result = Drug.objects.filter(illnesses__in=illnesses).distinct('id')
        return result