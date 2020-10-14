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

    def __str__(self):
        return self.content[:15]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:15]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, blank=True, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        item_type = self.comment
        if self.post:
            item_type = self.post

        return f"{self.user} liked {item_type.user}'s \
            {'post' if item_type == self.post else 'comment'}: {item_type.id}"


class Follower(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followee")
    following_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower")

    def __str__(self):
        return f"{self.user} is following {self.following_user}"
