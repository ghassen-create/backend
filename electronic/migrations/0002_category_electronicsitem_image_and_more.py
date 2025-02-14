# Generated by Django 4.2 on 2023-04-30 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='electronicsitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shops/items/'),
        ),
        migrations.AlterField(
            model_name='electronicsitem',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='electronic.electronicsshop'),
        ),
        migrations.AddField(
            model_name='electronicsitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='electronic.category'),
        ),
    ]
