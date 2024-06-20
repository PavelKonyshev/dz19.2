# Generated by Django 5.0.6 on 2024-06-20 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(
                    2024, 6, 20, 11, 56, 18, 890015, tzinfo=datetime.timezone.utc
                ),
                help_text="Укажите дату создания",
                null=True,
                verbose_name="Дата создания",
            ),
        ),
    ]
