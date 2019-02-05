# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, Media, Address
from django_reverse_admin import ReverseModelAdmin
# https://github.com/anziem/django_reverse_admin


class MediaInline(admin.StackedInline):
    # (admin.TabularInline) horizontal
    # (admin.StackedInline) vertical, se ven los label
    model = Media
    extra = 1


class PersonAdmin(ReverseModelAdmin):
    inline_type = 'tabular'
    # inline_type can be either "tabular" or "stacked" for tabular and stacked inlines respectively.
    # 'tabular'  uno al lado del otro

    inline_reverse = [
        ('address', {'fields': ['address', 'city', 'state', 'country', 'zip_code']}),
                          ]

    list_display = ['id', '__str__', 'email', 'phone', 'sex', 'address',
                    'total_social_medias', 'active', 'fecha_alta', "provincia"]

    list_filter = ['active', 'gender']

    fieldsets = [
        ('Date information', {'fields': ['last_name', 'first_name', 'gender']
                              }
         ),

        ('Contact information', {'fields': [('email', 'phone')]
                                 }
         ),
        ("Is Activate ?", {'fields': ['active']
                           }
         ),

    ]

    empty_value_display = '-empty-'
    search_fields = ['last_name', 'first_name']
    inlines = [MediaInline]

    class Meta:
        model = User

    def provincia(self, obj):
        return obj.address.get_state_display()


class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'city', 'state', 'country', 'zip_code']


admin.site.register(User, PersonAdmin)
admin.site.register(Address, AddressAdmin)
