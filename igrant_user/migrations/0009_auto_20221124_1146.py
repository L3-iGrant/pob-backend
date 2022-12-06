# Generated by Django 3.0.7 on 2022-11-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igrant_user', '0008_auto_20221122_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='igrantuser',
            name='org',
            field=models.CharField(choices=[('NIL', 'Nil'), ('RAKSA_OY', 'Raksa Oy, Finland'), ('BYGG_AB', 'Bygg AB, Sweden'), ('BOLAGSVERKET_AB', 'Bolagsverket AB, Sweden'), ('STHLM_CONSTRUCTIONS_AB', 'Sthlm Constructions AB'), ('RAPID_BUILDERS', 'Rapid Builders')], default='NIL', max_length=250),
        ),
    ]