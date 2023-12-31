# Generated by Django 4.2 on 2023-07-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("opr", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("first_name", models.CharField(default="unknown", max_length=55)),
                ("last_name", models.CharField(default="unknown", max_length=55)),
                ("subject", models.CharField(default="marathi", max_length=55)),
                ("age", models.IntegerField(default=19)),
            ],
        ),
    ]
