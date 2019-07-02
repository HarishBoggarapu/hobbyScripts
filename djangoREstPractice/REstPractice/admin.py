from django.contrib import admin
from .models import SportsRoster


class SportsRosterAdmin(admin.ModelAdmin):
    list_display = ['coach', 'quaterback']


# Register your models here.
admin.site.register(SportsRoster, SportsRosterAdmin)
