# Generated by Django 2.2.22 on 2021-05-25 12:44

from django.db import migrations

def ensure_slug_unique(apps, schema_editor):
    """
    Make sure slug field is unique in the committees.
    Alter the duplicates if needed.
    """
    Committee = apps.get_model("committees", "Committee")
    for committee in Committee.objects.all().order_by('-id'):
        slug = committee.slug
        if Committee.objects.filter(slug=slug).exclude(id=committee.id).exists():
            if len(slug) + len(str(committee.id)) + 1 > 100:
                committee.slug = f'{slug[:(100-len(str(committee.id))-1)]}-{committee.id}'
            else:
                committee.slug = f'{slug}-{committee.id}'
            committee.save(update_fields=['slug'])

class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0005_officer_email'),
    ]

    operations = [
        migrations.RunPython(ensure_slug_unique),
    ]
