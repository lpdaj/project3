# Generated by Django 2.0.3 on 2018-12-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.FloatField(),
        ),
    ]
