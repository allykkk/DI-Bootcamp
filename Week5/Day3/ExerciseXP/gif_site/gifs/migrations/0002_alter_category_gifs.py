# Generated by Django 4.2.1 on 2023-05-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gifs',
            field=models.ManyToManyField(related_name='categories', to='gifs.gif'),
        ),
    ]
