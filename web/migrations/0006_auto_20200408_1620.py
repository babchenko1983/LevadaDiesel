# Generated by Django 3.0.5 on 2020-04-08 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200408_1618'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('id', 'url')},
        ),
    ]
