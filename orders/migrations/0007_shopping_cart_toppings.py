# Generated by Django 2.0.3 on 2018-12-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20181212_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.Toppings'),
        ),
    ]