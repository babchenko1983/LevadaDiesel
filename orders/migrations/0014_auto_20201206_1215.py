# Generated by Django 3.0.5 on 2020-12-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20201206_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('cash', 'Наличные'), ('Cash on delivery', 'Наложеный платеж'), ('Visa, Master Card', 'Visa, Master Card')], default='cash', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('self', 'Самовывоз'), ('dhl or dpd', 'Доставка по Польше 20 Zl.')], max_length=100),
        ),
    ]
