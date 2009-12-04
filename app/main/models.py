# -*- coding: utf-8 -*-
from django.db import models

class CompareValue(models.Model):
    CRITERION_CHOICE = (
        (1, u'Эфективность'),
        (2, u'Цена'),
        (3, u'Доступность'),
        (4, u'Фармдействие')
    )

    value = models.FloatField(u'Значение')
    left = models.ForeignKey('Drug', related_name=u'leftdrug_set')
    top = models.ForeignKey('Drug', related_name=u'topdrug_set')
    criterion = models.IntegerField(u'Критерий', choices=CRITERION_CHOICE)
    
    def __unicode__(self):
        return self.value

class Drug(models.Model):
    name = models.CharField(u'Название', max_length=255)
    latin_name = models.CharField(u'Латинское название', max_length=255)
    category = models.ForeignKey('ATCCategory', verbose_name=u'Категория')
    compaire = models.ManyToManyField('self', symmetrical=False, through=CompareValue)

    def __unicode__(self):
        return self.name

class ATCCategory(models.Model):
    code = models.CharField(u'Код', max_length=100)
    name = models.CharField(u'Название', max_length=255)

    def __unicode__(self):
        return self.code