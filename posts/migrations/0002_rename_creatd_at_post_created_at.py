# Generated by Django 4.0.1 on 2022-01-18 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creatd_at',
            new_name='created_at',
        ),
    ]
