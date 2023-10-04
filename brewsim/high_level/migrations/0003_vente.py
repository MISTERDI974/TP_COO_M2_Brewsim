# Generated by Django 4.2.5 on 2023-10-04 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "high_level",
            "0002_rename_durée_action_duree_remove_action_ingredient_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Vente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("benef", models.IntegerField()),
                (
                    "departement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="high_level.departement",
                    ),
                ),
            ],
        ),
    ]