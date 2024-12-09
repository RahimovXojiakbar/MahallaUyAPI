from django.contrib import admin
from unfold.admin import ModelAdmin
from . import models


@admin.register(models.Chairman)
class ChairmanAdmin(ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.MFY)
class MFYAdmin(ModelAdmin):
    list_display = ['id', 'title']


@admin.register(models.Neighborhood)
class NeighborhoodAdmin(ModelAdmin):
    list_display = ['id', 'title']


@admin.register(models.House)
class HouseAdmin(ModelAdmin):
    list_display = ['id', 'house_number']


@admin.register(models.Human)
class HumanAdmin(ModelAdmin):
    list_display = ['id', 'fullname']

    