# Generated by Django 3.0.6 on 2020-05-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='payPalID',
            field=models.TextField(default=''),
        ),
    ]
