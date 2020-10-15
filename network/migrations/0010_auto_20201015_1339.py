# Generated by Django 3.1.2 on 2020-10-15 13:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_auto_20201015_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='following_user',
            new_name='followed_user',
        ),
        migrations.AddField(
            model_name='comment',
            name='edit_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follower',
            name='edit_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='follower',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='edit_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
