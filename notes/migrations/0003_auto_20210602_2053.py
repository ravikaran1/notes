# Generated by Django 3.1.5 on 2021-06-02 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_querie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='querie',
            old_name='sno',
            new_name='sno1',
        ),
    ]