# Generated by Django 3.0.7 on 2022-11-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0004_remove_requirement_submission_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='issuer_logo_url',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
