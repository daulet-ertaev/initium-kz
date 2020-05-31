# Generated by Django 3.0.6 on 2020-05-30 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('it', 'IT'), ('sport', 'Sport'), ('health', 'Health'), ('electronic', 'Electronic'), ('transport', 'Transport'), ('culture', 'Culture'), ('games', 'Games and Entertainment'), ('food', 'Food and Craft'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
