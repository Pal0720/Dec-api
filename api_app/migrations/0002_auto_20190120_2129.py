# Generated by Django 2.1.4 on 2019-01-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_level',
            field=models.PositiveIntegerField(),
        ),
    ]