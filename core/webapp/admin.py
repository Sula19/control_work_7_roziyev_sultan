from django.contrib import admin
from webapp.models import GuessBook


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'status', 'created_at', 'updated_at']
    list_filter = ['id', 'created_at', 'status', 'updated_at']
    search_fields = ['name', 'status', 'created_at', 'updated_at']
    fields = ['name', 'email', 'text', 'status']
    readonly_fields = ['created_at']


admin.site.register(GuessBook, BookAdmin)
