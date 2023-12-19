from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
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
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blogger = request.user
            comment.blog_post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval.'
            )

    comment_form = CommentForm()
    print("About to render template")

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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(post_status=1)
        post = get_object_or_404(queryset, post_slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.blogger == request.user:
            comment = comment_form.save(commit=False)
            comment.blog_post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(post_status=1)
    post = get_object_or_404(queryset, post_slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.blogger == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class AddPost(generic.CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = ('blogger', 'post_title', 'post_slug', 'post_image', 'excerpt', 'post_content', 'post_status')