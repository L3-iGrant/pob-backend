# Generated by Django 3.0.7 on 2022-11-13 10:16

from django.db import migrations
import django_jsonfield_backport.models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20221110_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responses',
            name='presentation_record',
            field=django_jsonfield_backport.models.JSONField(blank=True, default=[], null=True),
        ),
    ]