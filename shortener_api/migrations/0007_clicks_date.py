# Generated by Django 2.1.7 on 2023-02-01 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_api', '0006_remove_clicks_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='clicks',
            name='date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
