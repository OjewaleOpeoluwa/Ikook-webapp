# Generated by Django 3.2.16 on 2022-10-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_chefprofile_mealprep_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefprofile',
            name='is_chef',
            field=models.BooleanField(default=True),
        ),
    ]