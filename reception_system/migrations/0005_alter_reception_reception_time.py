# Generated by Django 4.2.6 on 2024-11-07 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reception_system", "0004_rename_teble_number_seat_table_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reception",
            name="reception_time",
            field=models.DateTimeField(verbose_name="利用開始時間"),
        ),
    ]
