from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.http import HttpResponseRedirect
from django.urls import reverse
from ckeditor.fields import RichTextField


STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
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
    blog_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-posted_on"]

    def __str__(self):
        return f"Comment: {self.body} | By: {self.blogger}"