from django.contrib import admin
from .models import Station, Track


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'active', 'paid', 'created_date')
    list_editable = ('order', 'paid', 'active')
    list_filter = ('paid', 'active', 'created_date')
    search_fields = ('name',)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date')
    search_fields = ('name',)
