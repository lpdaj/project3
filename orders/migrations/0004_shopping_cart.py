# Generated by Django 2.0.3 on 2018-12-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_toppings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('order', models.ManyToManyField(blank=True, related_name='orders', to='orders.Pizza')),
            ],
        ),
    ]
