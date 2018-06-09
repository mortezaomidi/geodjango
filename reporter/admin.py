# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Incidences, Counties, BlueEarth
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
    list_display = 'name', 'location'

class CountiesAdmin(LeafletGeoAdmin):
    list_display = 'counties', 'codes'

class SoilsAdmin(LeafletGeoAdmin):
    list_display = 'areasymbol', 'spatialver'

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)
admin.site.register(BlueEarth, SoilsAdmin)
