# Generated by Django 3.1.4 on 2021-01-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='track',
            field=models.TextField(default='unknown track', max_length=50),
        ),
        migrations.AlterField(
            model_name='audio',
            name='author',
            field=models.TextField(default='unknown author', max_length=50),
        ),
        migrations.AlterField(
            model_name='audio',
            name='file',
            field=models.FilePathField(path='media/mp3'),
        ),
    ]
