# Generated by Django 3.1.2 on 2020-10-13 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_follower_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='followed_users',
            new_name='following_user',
        ),
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followee', to=settings.AUTH_USER_MODEL),
        ),
    ]
