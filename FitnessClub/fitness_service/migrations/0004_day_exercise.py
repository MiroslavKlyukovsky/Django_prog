# Generated by Django 4.2 on 2023-05-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fitness_service", "0003_remove_abonement_iseven"),
    ]

    operations = [
        migrations.AddField(
            model_name="day",
            name="exercise",
            field=models.CharField(default="sport", max_length=20),
        ),
    ]