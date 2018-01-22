from django.contrib import admin
from publisher import models
# Register your models here.

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['Pub_name','address','website']
    search_fields = ['Pub_name','address','website']
    list_filter = ['Pub_name']

admin.site.register(models.Publisher,PublisherAdmin)