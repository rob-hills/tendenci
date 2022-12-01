# Generated by Django 3.2.12 on 2022-12-01 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainings', '0002_auto_20221130_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutsideSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(db_index=True, max_length=150)),
                ('date', models.DateField()),
                ('credits', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('description', models.TextField(blank=True, default='')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('update_dt', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('status_detail', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('disapproved', 'Disapproved')], default='pending', max_length=15, verbose_name='Status')),
                ('creator', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='outside_schools_created', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='outside_schools_updated', to=settings.AUTH_USER_MODEL)),
                ('school_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainings.schoolcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Outside School',
                'verbose_name_plural': 'Outside Schools',
            },
        ),
    ]
