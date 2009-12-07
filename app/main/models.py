# -*- coding: utf-8 -*-
from django.db import models

CRITERION_CHOICE = (
    (1, u'Эфективность'),
    (2, u'Цена'),
    (3, u'Доступность'),
    (4, u'Фармдействие')
)

class CompareValue(models.Model):
    value = models.FloatField(u'Значение')
    left = models.ForeignKey('Drug', related_name=u'leftdrug_set')
    top = models.ForeignKey('Drug', related_name=u'topdrug_set')
    criterion = models.IntegerField(u'Критерий', choices=CRITERION_CHOICE)
    
    def __unicode__(self):
        return self.value
    
    @classmethod
    def create(cls, criterion, top, left, value):
        try:
            obj = CompareValue.objects.filter(criterion=criterion).filter(left__pk=left).filter(top__pk=top).get()
        except cls.DoesNotExist:
            obj = cls(criterion=criterion)
        obj.left = Drug.objects.get(pk=left)
        obj.top = Drug.objects.get(pk=top)
        if left == top:
            obj.value = 1
        else:
            obj.value = value  
        return obj          
    
    @classmethod
    def set_value(cls, criterion, top, left, value):
        obj = cls.create(criterion, top, left, value)
        obj.save()
        if not obj.top == obj.left:
            nobj = cls.create(criterion, left, top, -value)
            nobj.save()
    
    @classmethod
    def grit_row(cls, criterion, pk, pks):
        items = cls.objects.filter(criterion=criterion[0]).filter(left=pk).filter(top__in=pks)
        obj = {
            'criterion': criterion[1],
            'criterion_pk': criterion[0]     
        }
        for item in items:
            obj[item.top.store_column] = int(item.value)
        return obj
        

class Drug(models.Model):
    name = models.CharField(u'Название', max_length=255)
    latin_name = models.CharField(u'Латинское название', max_length=255)
    category = models.ForeignKey('ATCCategory', verbose_name=u'Категория')
    compaire = models.ManyToManyField('self', symmetrical=False, through=CompareValue)

    def __unicode__(self):
        return self.name
    
    def tree_node(self):
        return {
            'id': 'd_%s' % self.pk,
            'text': self.name,
            'leaf': True,
            'cls': 'file',
            'pk': self.pk
        }
    
    @property    
    def store_column(self):
        return 'dr_%s' % self.pk
    
class ATCCategory(models.Model):
    code = models.CharField(u'Код', max_length=100)
    name = models.CharField(u'Название', max_length=255)

    def __unicode__(self):
        return self.code
    
    def tree_node(self):
        return {
            'id': 'c_%s' % self.pk,
            'text': '%s %s' % (self.code, self.name),
            'cls': 'folder',
            'children': [item.tree_node() for item in self.drug_set.all()],
            'expanded': True            
        }      