# Generated by Django 4.1.6 on 2023-02-13 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_rename_kvarira_kvartira'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kvartira',
            name='house_ptr',
        ),
        migrations.DeleteModel(
            name='Dacha',
        ),
        migrations.DeleteModel(
            name='House',
        ),
        migrations.DeleteModel(
            name='Kvartira',
        ),
    ]
