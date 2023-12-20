from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Permission
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.urls import reverse_lazy


class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts. 
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`blog/index.html`
    """
    queryset = Post.objects.filter(post_status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`

    **Template:**

    :template:`blog/post_detail.html`
    """
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
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
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
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(post_status=1)
    post = get_object_or_404(queryset, post_slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.blogger == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

    def form_valid(self, form):
        form.instance.blogger = self.request.user
        return super().form_valid(form)


class EditPost(generic.UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = (
        'post_title', 'post_slug', 'post_image', 'excerpt', 'post_content'
        )


class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')


@login_required
@permission_required('blog.add_post', raise_exception=True)
def add_post(request):
    from django.contrib.auth.models import User
    user = User.objects.get(username='CodeInstitute')
    from django.contrib.auth.models import Permission
    permission = Permission.objects.get(codename='add_post')
    user.user_permissions.add(permission)

    from django.contrib.auth.models import User
    user = User.objects.get(username='James')
    from django.contrib.auth.models import Permission
    permission = Permission.objects.get(codename='add_post')
    user.user_permissions.add(permission)
