# Generated by Django 4.2.1 on 2023-06-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_alter_rental_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='rental_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
