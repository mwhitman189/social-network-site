# Generated by Django 3.1.2 on 2020-10-13 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20201013_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='following_user',
        ),
        migrations.AddField(
            model_name='follower',
            name='following_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='network.user'),
            preserve_default=False,
        ),
    ]
