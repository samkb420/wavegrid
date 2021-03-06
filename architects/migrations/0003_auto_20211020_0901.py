# Generated by Django 3.2.8 on 2021-10-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architects', '0002_auto_20211020_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='client',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
