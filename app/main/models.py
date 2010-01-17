# -*- coding: utf-8 -*-
from django.db import models
from criterion import CRITERION_CHOICE
from django.core.urlresolvers import reverse

class Illness(models.Model):
    name = models.CharField(u'Название', max_length=255)
    
    def __unicode__(self):
        return self.name
    
    def tree_node(self):
        return {
            'id': 'ill_%s' % self.pk,
            'text': self.name,
            'leaf': True,
            'cls': 'file',
            'checked': False,
            'pk': self.pk
        }    

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
            obj = cls.objects.filter(criterion=criterion).filter(left__pk=left).filter(top__pk=top).get()
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
        value = cls.view_to_db(value)
        obj = cls.create(criterion, top, left, value)
        obj.save()
        if not obj.top == obj.left:
            nobj = cls.create(criterion, left, top, -value)
            nobj.save()
    
    @classmethod
    def grit_row(cls, criterion, pk, pks):
        drugs = Drug.objects.filter(pk__in=pks)
        items = cls.objects.filter(criterion=criterion[0]).filter(left=pk).filter(top__in=pks)
        obj = {
            'criterion': criterion[1],
            'criterion_pk': criterion[0]     
        }
        for item in items:
            obj[item.top.store_column] = cls.db_to_view(item.value)
        for item in drugs:
            if not item.store_column in obj:
                obj[item.store_column] = '1' 
        return obj
    
    @classmethod
    def matrix_row(cls, criterion, pk, pks):  
        items = cls.objects.filter(criterion=criterion[0]).filter(left=pk).filter(top__in=pks)
        values = {}
        for item in items:
            values[item.top.pk] = cls.db_to_python(item.value)
        output = []
        for item in pks:
            if not item in values:
                values[item] = 1 
            output.append(values[item])        
        return output
    
    @classmethod 
    def db_to_python(cls, value):
        value = float(value)
        if value < 1:
            value = 1 / abs(value)
        return value
    
    @classmethod
    def db_to_view(cls, value):
        if value >= 0:
            return value
        else:
            return '1/%i' % abs(value)
    
    @classmethod
    def view_to_db(cls, value):
        try:
            return int(value)
        except ValueError:
            return -int(value.split('/')[1])
        
class Drug(models.Model):
    name = models.CharField(u'Название', max_length=255)
    latin_name = models.CharField(u'Латинское название', max_length=255)
    category = models.ForeignKey('FarmAction', verbose_name=u'Категория')
    compaire = models.ManyToManyField('self', symmetrical=False, through=CompareValue)
    illnesses = models.ManyToManyField(Illness, verbose_name=u'Показания')

    def __unicode__(self):
        return '%s %s' % (self.pk, self.name)
    
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
    
class FarmAction(models.Model):
    name = models.CharField(u'Название', max_length=255)

    def __unicode__(self):
        return self.name
    
    def client_farm_tree_node(self):
        return {
            'id': 'f_%s' % self.pk,
            'text': self.name,
            'leaf': True,
            'pk': self.pk         
        } 
            
    def farm_tree_node(self):
        return {
            'id': 'f_%s' % self.pk,
            'text': self.name,
            'leaf': True,
            'url': '%s?pk=%s' % (reverse('main:index'), self.pk)         
        }  
            
    def tree_node(self):
        return {
            'id': 'c_%s' % self.pk,
            'text': self.name,
            'cls': 'folder',
            'children': [item.tree_node() for item in self.drug_set.all()],
            'expanded': True            
        }      