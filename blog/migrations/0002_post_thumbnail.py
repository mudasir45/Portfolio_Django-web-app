# Generated by Django 4.2.4 on 2023-08-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='img.png', null=True, upload_to='blog/images'),
        ),
    ]
