# Generated by Django 3.2.16 on 2022-10-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20221026_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='menuGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_photo', models.ImageField(blank=True, null=True, upload_to='uploads/menu/gallery/%Y/%m/%d/')),
            ],
        ),
    ]
