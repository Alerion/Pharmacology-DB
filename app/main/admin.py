# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Drug, ATCCategory
from django.http import HttpResponse

class DrugAdmin(admin.ModelAdmin):


    def edit_vector(self, request, pk):
        return HttpResponse('Hello %s' % pk)

    def get_urls(self):
        from django.conf.urls.defaults import patterns, url

        urls = super(DrugAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^em/(?P<pk>\d+)/$', self.admin_site.admin_view(self.edit_vector), name='edit_vector')
        )
        return my_urls + urls

admin.site.register(Drug, DrugAdmin)
admin.site.register(ATCCategory)