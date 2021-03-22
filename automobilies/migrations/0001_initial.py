# Generated by Django 3.1.7 on 2021-03-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Automobilie",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "plate",
                    models.CharField(max_length=8, verbose_name="Placa Automóvel"),
                ),
            ],
        ),
    ]
