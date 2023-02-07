# Generated by Django 2.1.7 on 2023-01-30 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('hash_url', models.URLField(unique=True)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
