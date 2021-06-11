# Generated by Django 2.2.22 on 2021-05-25 12:32

from django.db import migrations
import tendenci.apps.base.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0004_auto_20210525_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='slug',
            field=tendenci.apps.base.fields.SlugField(db_index=True, max_length=100, unique=True, verbose_name='URL Path'),
        ),
    ]