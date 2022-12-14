# Generated by Django 3.2.16 on 2022-10-30 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_setmenu_menu_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menugallery',
            name='banner_photo',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='setmenu',
            name='menu_gallery',
            field=models.ManyToManyField(related_name='gallery', to='menu.MenuGallery'),
        ),
    ]
