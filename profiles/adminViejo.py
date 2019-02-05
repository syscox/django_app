# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, Media, Address


class AdminUser(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'phone', 'gender', 'address', 'fecha_alta', 'total_social_medias', 'active']
    list_filter = ['active', 'gender']

    fieldsets = [
        ('Date information', {'fields': [('last_name', 'first_name'), 'gender']
                              }
         ),

        ('Contact information', {'fields': ['email', 'phone', 'address']
                                 }
         ),
        ("Is Activate ?", {'fields': ['active']
                              }
         ),
    ]
    empty_value_display = '-empty-'
    # list_display_links = ["name"] quiero que nombre sea mi link (azul)
    # list_editable = ['email']
    # me permite editar el mail desde la ventana principal
    search_fields = ['last_name', 'first_name']
    # se agrega un buscador encima

    class Meta:
        model = User


class AdminAddress(admin.ModelAdmin):
    list_display = ['__str__', 'address', 'city', 'state', 'country', 'zip_code']

    class Meta:
        model = Address


class AdminMedias(admin.ModelAdmin):
    list_display = ['name', 'url', 'user_id']

    class Meta:
        model = Media


admin.site.register(User, AdminUser)
admin.site.register(Address, AdminAddress)
admin.site.register(Media, AdminMedias)
