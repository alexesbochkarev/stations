from django.contrib import admin
from .models import Station


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'paid', 'created_date')
    list_editable = ('order', 'paid')
    list_filter = ('paid', 'created_date')
    search_fields = ('name',)
