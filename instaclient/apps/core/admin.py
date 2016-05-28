#-*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from core.models import HashTag, ImageUrl


class HashTagAdmin(admin.ModelAdmin):
    fieldsets = (
        (_(u'HashTag General Informations'), {
            'fields' : ('hashtag', 'search_count')
        }),
        (_(u'HashTag Status'), {
            'fields' : ('is_defective', 'created_time', 'updated_time')
        })
    )

    list_display = ('hashtag', 'search_count', 'created_time', 'updated_time', 'is_defective')
    list_filter = ('is_defective', 'created_time', 'updated_time')
    search_fields = ('hashtag',)
    ordering = ('updated_time',)
    readonly_fields = ('created_time', 'updated_time')


class ImageUrlAdmin(admin.ModelAdmin):
    fieldsets = (
        (_(u'Image Url General Informations'), {
            'fields' : ('url', 'hashtag')
        }),
        (_(u'Image Url Status'), {
            'fields' : ('created_time', 'updated_time')
        })
    )

    list_display = ('url', 'hashtag', 'created_time', 'updated_time', 'show_image_link', 'download_image_link')
    list_filter = ('created_time', 'updated_time')
    search_fields = ('hashtag',)
    ordering = ('updated_time',)
    readonly_fields = ('created_time', 'updated_time')


admin.site.register(HashTag, HashTagAdmin)
admin.site.register(ImageUrl, ImageUrlAdmin)
