from django.contrib import admin
from .models import Post, Comment, Personal
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
    list_filter = ('status', 'created_on')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'approved', 'created_on')
    search_fields = ('name', 'body')
    list_filter = ('created_on', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Personal)
