from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('post_title', 'post_slug', 'post_status')
    search_fields = ['post_title', 'post_content']
    list_filter = ('post_status', 'posted_on',)
    prepopulated_fields = {'post_slug': ('post_title',)}
    summernote_fields = ('post_content',)


admin.site.register(Comment)
