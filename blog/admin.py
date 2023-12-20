from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('post_title', 'post_slug', 'post_status')
    search_fields = ['post_title', 'post_content']
    list_filter = ('post_status', 'posted_on',)
    prepopulated_fields = {'post_slug': ('post_title',)}
    summernote_fields = ('post_content',)


admin.site.register(Comment)
