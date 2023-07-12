# Generated by Django 4.1 on 2023-06-10 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Peoples",
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
                ("first_name", models.CharField(max_length=250)),
                ("img_ppl", models.ImageField(upload_to="pics")),
                ("des_ppl", models.TextField()),
            ],
        ),
    ]
