from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_thumb', 'title', )
    readonly_fields = ('image_thumb', )


admin.site.register(Photo, PhotoAdmin)
