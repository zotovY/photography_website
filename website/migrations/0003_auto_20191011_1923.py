# Generated by Django 2.2.6 on 2019-10-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_presets_strong_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presets',
            name='img',
            field=models.ImageField(default=None, upload_to='media/presets/'),
        ),
    ]