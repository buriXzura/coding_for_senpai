# Generated by Django 2.1.7 on 2020-10-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0003_auto_20201027_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='nice'),
        ),
    ]
