# Generated by Django 3.2.7 on 2021-12-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitemanager', '0008_alter_newsblocks_borderselect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsblocks',
            name='borderSelect',
            field=models.CharField(choices=[('Blauw', 'Blauw'), ('Groen', 'Groen'), ('Rood', 'Rood'), ('Geen', 'Geen')], max_length=255),
        ),
    ]
