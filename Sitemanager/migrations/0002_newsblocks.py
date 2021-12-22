# Generated by Django 3.2.7 on 2021-12-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitemanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='newsImages')),
                ('alinea1', models.TextField(max_length=150)),
                ('alinea2', models.TextField(max_length=150)),
                ('alinea3', models.TextField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Niews blokken',
            },
        ),
    ]
