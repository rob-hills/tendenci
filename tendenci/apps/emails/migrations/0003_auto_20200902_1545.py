# Generated by Django 2.2.16 on 2020-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20180310_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='email',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
    ]
