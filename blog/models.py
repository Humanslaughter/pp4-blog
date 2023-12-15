from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    post_title = models.CharField(max_length=200, unique=True)
    post_slug = models.SlugField(max_length=200, unique=True)
    post_content = models.TextField()
    post_status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)