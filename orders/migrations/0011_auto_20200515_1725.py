# Generated by Django 3.0.5 on 2020-05-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200515_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='privacy',
            field=models.BooleanField(default=True),
        ),
    ]