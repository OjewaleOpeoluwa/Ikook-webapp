# Generated by Django 3.2.16 on 2022-10-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_remove_setmenu_menu_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='setmenu',
            name='menu_gallery',
            field=models.ManyToManyField(related_name='gallery', to='menu.MenuGallery'),
        ),
    ]
