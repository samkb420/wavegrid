# Generated by Django 3.2.8 on 2021-10-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architects', '0016_alter_projectimages_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
    ]
