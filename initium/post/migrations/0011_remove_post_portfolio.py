# Generated by Django 3.0.6 on 2020-05-31 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_post_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='portfolio',
        ),
    ]
