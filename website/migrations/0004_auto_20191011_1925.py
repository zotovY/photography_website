# Generated by Django 2.2.6 on 2019-10-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20191011_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presets',
            name='img',
            field=models.ImageField(default=None, upload_to='media/'),
        ),
    ]
