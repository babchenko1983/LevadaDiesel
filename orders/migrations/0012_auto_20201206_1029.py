# Generated by Django 3.0.5 on 2020-12-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200515_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('self', 'self delivery'), ('dhl or dpd', 'dhl or dpd')], default='self', max_length=100),
        ),
    ]
