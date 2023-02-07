# Generated by Django 2.1.7 on 2023-01-31 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_api', '0002_auto_20230131_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clicks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_url', models.URLField()),
                ('date_clicks', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='urls',
            name='clicks',
        ),
        migrations.AddField(
            model_name='clicks',
            name='clicks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener_api.Urls'),
        ),
    ]
