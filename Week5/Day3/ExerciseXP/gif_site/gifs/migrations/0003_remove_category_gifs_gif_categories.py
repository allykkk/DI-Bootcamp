# Generated by Django 4.2.1 on 2023-05-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0002_alter_category_gifs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='gifs',
        ),
        migrations.AddField(
            model_name='gif',
            name='categories',
            field=models.ManyToManyField(related_name='gifs', to='gifs.category'),
        ),
    ]
