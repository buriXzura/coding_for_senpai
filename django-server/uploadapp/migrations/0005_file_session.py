# Generated by Django 2.1.7 on 2020-10-29 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0004_auto_20201028_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='session',
            field=models.CharField(default='20', max_length=20),
        ),
    ]
