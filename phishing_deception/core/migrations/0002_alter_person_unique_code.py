# Generated by Django 5.1.2 on 2024-10-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='unique_code',
            field=models.TextField(null=True),
        ),
    ]
