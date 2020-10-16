from django.test import TestCase

from .models import User, Post, Comment, Follower, Like

# Create your tests here.


class NetworkTestCase(TestCase):
    """ Test cases for the social network app """

    def setUp(self):
        """ Initialize objects in the test DB """

        # Create users
        u1 = User.objects.create(
            username="Ronald", password="MacInDaHouse", is_superuser=True)
        u2 = User.objects.create(username="Dennis", password="GettinDenised")
        u3 = User.objects.create(username="SweetDee", password="You'reAbird")

        # Create posts
        p1 = Post.objects.create(
            user=u1, content="What will we do tonight, Brain?")
        p2 = Post.objects.create(
            user=u2, content="The same thing we do every night, Pinky...")
        p3 = Post.objects.create(user=u3, content="This is a suuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuupppppppeeeeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrr Loooooooooooooonnnnnnnnnnnnnnnnnnnnngggggggggggggggg ppppppppppppppppppppooooooooooooooooooooooossssssssssssssssssssssssstttttttttttttttt")
        p4 = Post.objects.create(
            user=u1, content="Try to take over the world?...")
        p5 = Post.objects.create(
            user=u2, content="No, Pinky. Try to take over the world!!!!")

        # Create comments
        c1 = Comment.objects.create(user=u1, content="Woozle Wazzle?")
        c2 = Comment.objects.create(
            user=u2, post=p3, comment=c1)
        c3 = Comment.objects.create(user=u3, post=p2)

        # Create likes
        l1 = Like.objects.create(user=u1, post=p2)
        l2 = Like.objects.create(user=u2, post=p2)
        l3 = Like.objects.create(user=u1, post=p2)
        l4 = Like.objects.create(user=u2, post=p4)

        # Create followers
        f1 = Follower.objects.create(user=u1, followed_user=u2)
        f2 = Follower.objects.create(user=u2, followed_user=u2)
        f3 = Follower.objects.create(user=u1, followed_user=u3)
        f4 = Follower.objects.create(user=u3, followed_user=u2)

    def test_valid_comment(self):
        """ Check that a valid comment is valid """
        c = Comment.objects.get(content="Woozle Wazzle?")
        self.assertTrue(c.is_valid_comment())

    def test_invalid_comment(self):
        """ Check that an invalid comment is invalid """
        c1 = Comment.objects.get(content="Woozle Wazzle?")
        c2 = Comment.objects.get(comment=c1)
        self.assertFalse(c2.is_valid_comment())

    def test_valid_like(self):
        """ Check that a valid like is valid """
        u = User.objects.get(username="Dennis")
        p = Post.objects.get(
            content="Try to take over the world?...")
        l = Like.objects.get(user=u, post=p)
        self.assertTrue(l.is_valid_like())

    def test_invalid_like(self):
        """ Check that an invalid like is invalid """
        u = User.objects.get(username="Dennis")
        p = Post.objects.get(
            content="The same thing we do every night, Pinky...")
        l = Like.objects.get(user=u, post=p)
        self.assertFalse(l.is_valid_like())

    def test_valid_like_count(self):
        """ Check that a valid like count (<2) is valid """
        u = User.objects.get(username="Dennis")
        p = Post.objects.get(
            content="The same thing we do every night, Pinky...")
        likes = Like.objects.filter(user=u, post=p)
        self.assertLess(likes.count(), 2)

    def test_invalid_like_count(self):
        """ Check that an invalid like count (>1) is invalid """
        u = User.objects.get(username="Ronald")
        p = Post.objects.get(
            content="The same thing we do every night, Pinky...")
        likes = Like.objects.filter(user=u, post=p)
        self.assertGreater(likes.count(), 1)

    def test_valid_follower(self):
        """ Check that a valid follower is valid """
        u1 = User.objects.get(username="Ronald")
        u2 = User.objects.get(username="Dennis")
        f = Follower.objects.get(user=u1, followed_user=u2)
        self.assertTrue(f.is_valid_follower())

    def test_invalid_follower(self):
        """ Check that an invalid follower is invalid """
        u = User.objects.get(username="Dennis")
        f = Follower.objects.get(user=u, followed_user=u)
        self.assertFalse(f.is_valid_follower())

    def test_follower_count(self):
        """ Check that a correct count of followers is found """
        u = User.objects.get(username="Dennis")
        followers = Follower.objects.filter(followed_user=u)
        self.assertEqual(followers.count(), 3)
