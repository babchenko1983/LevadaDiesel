# Generated by Django 3.0.5 on 2020-04-21 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
