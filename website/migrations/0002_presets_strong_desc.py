# Generated by Django 2.2.6 on 2019-10-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presets',
            name='strong_desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
