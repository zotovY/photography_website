# Generated by Django 2.2.6 on 2019-10-11 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Presets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PresetsExamples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before', models.ImageField(upload_to='')),
                ('after', models.ImageField(upload_to='')),
                ('preset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.Presets')),
            ],
        ),
    ]