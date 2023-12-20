from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = fields = (
            'post_title',
            'post_slug',
            'post_image',
            'excerpt',
            'post_content',
            'post_status'
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
