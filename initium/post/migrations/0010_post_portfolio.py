# Generated by Django 3.0.6 on 2020-05-31 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_donation_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='portfolio',
            field=models.ImageField(default='portfolioImages/default.png', upload_to='portfolioImages'),
        ),
    ]