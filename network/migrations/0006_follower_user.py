# Generated by Django 3.1.2 on 2020-10-13 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20201013_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='current_user', to='network.user'),
            preserve_default=False,
        ),
    ]
