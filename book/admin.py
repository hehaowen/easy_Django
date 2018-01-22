from django.contrib import admin
from book import models
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','publishers']
    search_fields = ['title']
    list_filter = ['publishers']


admin.site.register(models.Book,BookAdmin)