# Generated by Django 4.2.1 on 2023-06-01 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_alter_rental_rental_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
