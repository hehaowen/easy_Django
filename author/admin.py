from django.contrib import admin
from author import models
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['aut_name','hometown']
    search_fields = ['aut_name','hometown']
    list_filter = ['hometown']











admin.site.register(models.Author,AuthorAdmin)