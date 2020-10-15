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
