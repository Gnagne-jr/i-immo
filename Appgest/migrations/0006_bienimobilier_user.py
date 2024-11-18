# Generated by Django 5.1.3 on 2024-11-17 23:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Appgest", "0005_rename_est_agent_customuser_is_agent_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bienimobilier",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
