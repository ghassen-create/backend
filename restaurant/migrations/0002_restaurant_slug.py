# Generated by Django 4.2 on 2023-04-28 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
