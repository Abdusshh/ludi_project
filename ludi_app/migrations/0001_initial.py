# Generated by Django 5.0.6 on 2024-05-18 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Simulation",
            fields=[
                (
                    "simulation_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("simulation_name", models.CharField(max_length=255)),
                ("company_id", models.IntegerField()),
                ("company_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.IntegerField(primary_key=True, serialize=False)),
                ("user_name", models.CharField(max_length=255)),
                ("user_surname", models.CharField(max_length=255)),
                ("signup_datetime", models.DateTimeField()),
                ("progress_percent", models.IntegerField()),
                (
                    "simulation",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ludi_app.simulation",
                    ),
                ),
            ],
        ),
    ]
