from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models

@admin.register(models.Neighborhood)
class NeighborhoodAdmin(ModelAdmin):
    list_display = ['id', 'title', 'chairman','MFY']


@admin.register(models.House)
class HouseAdmin(ModelAdmin):
    list_display = ['house_boss', 'house_number', 'a_b']
