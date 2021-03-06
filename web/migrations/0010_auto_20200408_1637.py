# Generated by Django 3.0.5 on 2020-04-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20200408_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('number', 'url')},
        ),
    ]
