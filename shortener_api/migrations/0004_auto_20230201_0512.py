# Generated by Django 2.1.7 on 2023-02-01 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_api', '0003_auto_20230201_0339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clicks',
            name='clicks',
        ),
        migrations.AddField(
            model_name='urls',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Clicks',
        ),
    ]
