# Generated by Django 3.2.16 on 2022-10-24 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='mobile_number',
            new_name='phone_no',
        ),
    ]
