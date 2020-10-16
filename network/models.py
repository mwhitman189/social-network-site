from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    timestamp = models.DateTimeField(
        auto_now_add=True, editable=False, null=False, blank=False)
    edit_timestamp = models.DateTimeField(
        auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.content[:15]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=50)
    post = models.ForeignKey(
        Post, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        'self', null=True, on_delete=models.CASCADE, related_name="+")
    timestamp = models.DateTimeField(
        auto_now_add=True, editable=False, null=False, blank=False)
    edit_timestamp = models.DateTimeField(
        auto_now=True, editable=False, null=False, blank=False)

    def is_valid_comment(self):
        return self.post == None if self.comment else self.comment == None

    def __str__(self):
        return self.content[:15]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, blank=True, null=True, on_delete=models.CASCADE)

    def is_valid_like(self):
        item_type = self.comment
        if self.post:
            item_type = self.post

        return self.user != item_type.user

    def __str__(self):
        item_type = self.comment
        if self.post:
            item_type = self.post

        return f"{self.user} liked {item_type.user}'s \
            {'post' if item_type == self.post else 'comment'}: {item_type.id}"


class Follower(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower")
    followed_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followed_user")
    timestamp = models.DateTimeField(
        auto_now_add=True, editable=False, null=False, blank=False)
    edit_timestamp = models.DateTimeField(
        auto_now=True, editable=False, null=False, blank=False)

    def is_valid_follower(self):
        return self.user != self.followed_user

    def __str__(self):
        return f"{self.user.username} is following {self.followed_user.username}"
