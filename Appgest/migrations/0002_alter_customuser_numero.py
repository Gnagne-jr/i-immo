# Generated by Django 5.1.3 on 2024-11-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Appgest", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="numero",
            field=models.IntegerField(),
        ),
    ]
