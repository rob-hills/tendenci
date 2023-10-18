# Generated by Django 3.2.19 on 2023-10-17 14:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0030_registrationconfiguration_reply_to_receive_notices'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualEventCreditsLogicConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_period', models.PositiveSmallIntegerField(default=50, help_text='Number of minutes to earn 1 full credit.', verbose_name='Period (Number of Minutes per Credits Earned)')),
                ('credit_period_questions', models.PositiveSmallIntegerField(default=4, help_text='Total number of questions per credit period.', verbose_name='Number of Questions for each credit period')),
                ('full_credit_percent', models.DecimalField(blank=True, decimal_places=2, help_text='Per period. Leave blank if using number of questions.', max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Percent of Questions Correct for Full Credit')),
                ('full_credit_questions', models.PositiveSmallIntegerField(blank=True, help_text='Per period. Leave blank if using percentage.', null=True, verbose_name='Number of Questions for Full Credit')),
                ('half_credits_allowed', models.BooleanField(default=True, verbose_name='Half Credits Allowed')),
                ('half_credit_periods', models.PositiveSmallIntegerField(default=0, help_text='Leave 0 if allowed for entirety of event', verbose_name='Number of Periods after which Half Credits Can be Earned')),
                ('half_credit_credits', models.PositiveIntegerField(default=0, help_text='Leave 0 if there is no requirement.', verbose_name='Number of full credits required before half credits can be earned.')),
            ],
            options={
                'verbose_name': 'Virtual Event Credits Logic Configuration',
                'verbose_name_plural': 'Virtual Event Credits Logic Configuration',
            },
        ),
        migrations.CreateModel(
            name='ZoomAPIConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(help_text='Used to easily identify this Zoom account.', max_length=255)),
                ('sdk_client_id', models.CharField(help_text='Client ID for Zoom SDK app (to launch Zoom from Event).', max_length=100)),
                ('sdk_client_secret', models.CharField(help_text='Client secret for Zoom SDK app (to launch Zoom from Event).', max_length=255)),
                ('oauth_account_id', models.CharField(help_text='Account ID for Zoom Server to Server OAuth app (get meeting/webinar info).', max_length=100)),
                ('oauth_client_id', models.CharField(help_text='Client ID for Zoom Server to Server OAuth app (get meeting/webinar info).', max_length=100)),
                ('oauth_client_secret', models.CharField(help_text='Client secret for Zoom Server to Server Oauth app (get meeting/webinar info).', max_length=255)),
                ('use_as_default', models.BooleanField(default=False, help_text='Check to use this as the default option when selecting a Zoom API Configuration. Only one configuration can be used as default.')),
            ],
            options={
                'verbose_name': 'Zoom API Configuration',
                'verbose_name_plural': 'Zoom API Configurations',
            },
        ),
        migrations.AddField(
            model_name='place',
            name='is_zoom_webinar',
            field=models.BooleanField(default=False, help_text='Check if the Zoom meeting is a webinar.'),
        ),
        migrations.AddField(
            model_name='place',
            name='use_zoom_integration',
            field=models.BooleanField(default=False, help_text='Use Zoom integration to allow launching Zoom meeting from Event.<br />Note: The credits generated via Zoom meeting can override those specified under the Credits tab.'),
        ),
        migrations.AddField(
            model_name='place',
            name='zoom_meeting_id',
            field=models.CharField(blank=True, help_text='Zoom meeting ID for this Event.', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='zoom_meeting_passcode',
            field=models.CharField(blank=True, help_text='Zoom meeting passcode for this Event.', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='zoom_api_configuration',
            field=models.ForeignKey(blank=True, help_text="Zoom API credentials for the account you want to use for this Event's meeting.", null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.zoomapiconfiguration'),
        ),
    ]