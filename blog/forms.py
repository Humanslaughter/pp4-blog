from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    """
    Form class for users to make a post 
    """
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
    """
    Form class for users to comment on a post 
    """
    class Meta:
        model = Comment
        fields = ('body',)
