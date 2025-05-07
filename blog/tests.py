from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Post, Comment
from django.contrib.auth.models import User

class PostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(title="Test Post", content="Test content", author=self.user)
        self.list_url = reverse('post-list-create')
        self.detail_url = reverse('post-detail', kwargs={'pk': self.post.id})
        self.comment_create_url = reverse('comment-create', kwargs={'post_id': self.post.id})
        self.comment_list_url = reverse('comment-list', kwargs={'post_id': self.post.id})

    def test_list_posts(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        data = {'title': 'New Post', 'content': 'New content'}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_retrieve_post(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_update_post(self):
        data = {'title': 'Updated Title', 'content': 'Updated content'}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')

    def test_delete_post(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_create_comment(self):
        data = {'content': 'This is a test comment'}
        response = self.client.post(self.comment_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().author, self.user)

    def test_list_comments(self):
        # Create a comment first
        Comment.objects.create(post=self.post, content="First comment", author=self.user)
        Comment.objects.create(post=self.post, content="Second comment", author=self.user)
        response = self.client.get(self.comment_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)