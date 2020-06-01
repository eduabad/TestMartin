from django.contrib import admin
from .models import *


class HeroeAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'real_name', 'publisher']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'founder')


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Heroe, HeroeAdmin)


