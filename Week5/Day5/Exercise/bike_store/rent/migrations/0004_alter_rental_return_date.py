# Generated by Django 4.2.1 on 2023-06-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_alter_customer_phone_number_rentalrate_rental'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]