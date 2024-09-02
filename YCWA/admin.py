from django.contrib import admin

from YCWA.models import Entry


# Register your models here.


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'content', 'id')