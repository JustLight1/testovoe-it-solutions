from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'views_count', 'position')
    list_filter = ('position',)
    search_fields = ('title',)
    ordering = ('position',)
