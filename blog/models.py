from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


STATUS = ((0, "Draft"), (1, "Published"))




class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    blogger = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    post_title = models.CharField(max_length=200, unique=True)
    post_slug = models.SlugField(max_length=200, unique=True)
    post_image = CloudinaryField('image', default='placeholder')
    post_content = RichTextField(blank=True, null=True)
    post_status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-posted_on"]

    def __str__(self):
        return f"{self.post_title} | {self.blogger}"

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    blog_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    blogger = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-posted_on"]

    def __str__(self):
        return f"Comment: {self.body} | By: {self.blogger}"
