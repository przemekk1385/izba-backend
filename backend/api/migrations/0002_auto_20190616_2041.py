# Generated by Django 2.2.1 on 2019-06-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured',
        ),
        migrations.AlterField(
            model_name='post',
            name='header',
            field=models.FilePathField(path='media'),
        ),
    ]
