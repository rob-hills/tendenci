# Generated by Django 2.2.20 on 2021-05-07 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0002_chapter_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='email',
            field=models.EmailField(blank=True, max_length=120, null=True),
        ),
    ]
