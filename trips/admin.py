from django.contrib.gis import admin
from django.utils.html import format_html
from .models import Trip, Location, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    fields = ['image', 'caption', 'taken_at', 'thumbnail_preview']
    readonly_fields = ['thumbnail_preview']

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:60px;border-radius:4px;">', obj.image.url)
        return '-'
    thumbnail_preview.short_description = 'Előnézet'


class LocationInline(admin.StackedInline):
    model = Location
    extra = 0
    fields = ['name', 'description', 'point', 'order', 'visited_at']


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'location_count', 'created_at']
    list_filter = ['start_date']
    search_fields = ['name', 'description']
    inlines = [LocationInline]
    date_hierarchy = 'start_date'

    def location_count(self, obj):
        return obj.locations.count()
    location_count.short_description = 'Helyszínek'


@admin.register(Location)
class LocationAdmin(admin.GISModelAdmin):
    list_display = ['name', 'trip', 'order', 'visited_at']
    list_filter = ['trip']
    search_fields = ['name', 'description', 'trip__name']
    ordering = ['trip', 'order']
    inlines = [PhotoInline]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_preview', 'caption', 'location', 'taken_at']
    list_filter = ['location__trip']
    search_fields = ['caption', 'location__name']
    readonly_fields = ['thumbnail_preview']

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:60px;border-radius:4px;">', obj.image.url)
        return '-'
    thumbnail_preview.short_description = 'Kép'
