# Generated by Django 4.2 on 2023-04-26 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_clothingitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothingitem',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Homme'), ('female', 'Femme')], max_length=80, null=True),
        ),
    ]