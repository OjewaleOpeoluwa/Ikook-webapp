# Generated by Django 3.2.16 on 2022-11-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20221030_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setmenu',
            name='menu_gallery',
            field=models.ManyToManyField(related_name='gallery', to='menu.MenuGallery'),
        ),
    ]