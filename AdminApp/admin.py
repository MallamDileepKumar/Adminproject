from django.contrib import admin
from .models import Products
# Register your models here.
class PDAdmin(admin.ModelAdmin):
    list_display = ('PID', 'PName', 'PCost', 'MfDate', 'EPDate')
    list_filter = ('PName', 'PCost',)
    list_editable = ('PName', 'PCost',)
admin.site.register(Products, PDAdmin)
