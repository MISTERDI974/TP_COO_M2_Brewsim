# Generated by Django 4.2.5 on 2023-09-27 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Action",
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
                ("commande", models.CharField(max_length=100)),
                ("durée", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Departement",
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
                ("numero", models.IntegerField()),
                ("prix_m2", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
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
                ("nom", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Machine",
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
                ("nom", models.CharField(max_length=100)),
                ("prix", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="QuantiteIngredient",
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
                ("quantite", models.IntegerField()),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="high_level.ingredient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recette",
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
                ("nom", models.CharField(max_length=100)),
                (
                    "action",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="high_level.action",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usine",
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
                ("taille", models.IntegerField()),
                (
                    "departement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="high_level.departement",
                    ),
                ),
                ("machine", models.ManyToManyField(to="high_level.machine")),
                ("recette", models.ManyToManyField(to="high_level.recette")),
                ("stock", models.ManyToManyField(to="high_level.quantiteingredient")),
            ],
        ),
        migrations.CreateModel(
            name="Prix",
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
                ("prix", models.IntegerField()),
                (
                    "departement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="high_level.departement",
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="high_level.ingredient",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="action",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="high_level.ingredient"
            ),
        ),
        migrations.AddField(
            model_name="action",
            name="machine",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="high_level.machine"
            ),
        ),
    ]
