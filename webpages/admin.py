from django.contrib import admin
from . models import Slider, Team

# Register your models here.
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('headline', 'subtitle', 'button_text')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'role',)
