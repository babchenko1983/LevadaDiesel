# Generated by Django 3.0.5 on 2020-04-08 13:33

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20200408_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.SlugField(default=builtins.id, unique=True),
        ),
    ]
