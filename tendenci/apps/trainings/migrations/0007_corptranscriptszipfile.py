# Generated by Django 3.2.16 on 2023-01-20 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tendenci.apps.base.fields
import tendenci.apps.trainings.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainings', '0006_auto_20230109_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorpTranscriptsZipFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp_profile_id', models.IntegerField()),
                ('params_dict', tendenci.apps.base.fields.DictField(verbose_name='Parameters Dict')),
                ('start_dt', models.DateTimeField(auto_now_add=True)),
                ('finish_dt', models.DateTimeField(blank=True, null=True)),
                ('zip_file', models.FileField(upload_to=tendenci.apps.trainings.models.get_transcript_zip_file_path)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]