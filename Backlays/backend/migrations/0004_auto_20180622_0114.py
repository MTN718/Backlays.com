# Generated by Django 2.0.6 on 2018-06-21 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20180622_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='base',
            old_name='app_name',
            new_name='name',
        ),
    ]
