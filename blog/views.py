from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(post_status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    
    queryset = Post.objects.filter(post_status=1)
    post = get_object_or_404(queryset, post_slug=slug)
    comments = post.comments.all().order_by("-posted_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blogger = request.user
            comment.blog_post = post
            comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )