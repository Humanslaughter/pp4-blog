from django.test import TestCase
from .forms import PostForm, CommentForm


class TestPostForm(TestCase):

    def test_form_is_valid(self):
        post_form = PostForm({
            'post_title': 'This is a great post',
            'post_slug': 'this-is-a-great-post',
            'excerpt': 'This is a great excerpt',
            'post_content': 'This is a great post',
            'post_status': '1'
        })
        self.assertTrue(post_form.is_valid(), msg="Form is invalid")

        def test_form_is_invalid(self):
            post_form = PostForm({
                'post_title': '',
                'post_slug': '',
                'excerpt': '',
                'post_content': '',
                'post_status': ''
            })
            self.assertFalse(post_form.is_valid(), msg="Form is valid")

class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")

        def test_form_is_invalid(self):
            comment_form = CommentForm({'body': ''})
            self.assertFalse(comment_form.is_valid(), msg="Form is valid")