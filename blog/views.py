from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(post_status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    
    queryset = Post.objects.filter(post_status=1)
    post = get_object_or_404(queryset, post_slug=slug)
    comments = post.comments.all().order_by("-posted_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
        },
    )