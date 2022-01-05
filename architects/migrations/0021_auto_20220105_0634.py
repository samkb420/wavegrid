# Generated by Django 3.2.8 on 2022-01-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architects', '0020_auto_20220105_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='projectimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
