# Generated by Django 3.2.8 on 2021-10-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architects', '0010_alter_projectimages_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimages',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
