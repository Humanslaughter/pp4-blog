from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = Post(post_title="Blog post_title", blogger=self.user,
                         post_slug="blog-post_title", excerpt="Blog excerpt",
                         post_content="Blog post_content", post_status=1)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'post_detail', args=['blog-post_title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog post_title", response.content)
        self.assertIn(b"Blog post_content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'post_detail', args=['blog-post_title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )

    def test_successful_post_submission(self):
        """Test for adding a new post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'post_title': 'This is a test post',
            'post_slug': 'this-is-a-test-post',
            'post_content': 'Blog post content.',
            'post_status': '1',
            'excerpt': 'This is a test post excerpt.',
        }
        response = self.client.post(reverse(
            'home'))