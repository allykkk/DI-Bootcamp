# Generated by Django 4.2.1 on 2023-05-31 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date_completion',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
