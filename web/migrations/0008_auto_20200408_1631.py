# Generated by Django 3.0.5 on 2020-04-08 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20200408_1630'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('id', 'url')},
        ),
    ]
