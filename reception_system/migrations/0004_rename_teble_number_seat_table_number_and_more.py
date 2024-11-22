# Generated by Django 4.2.6 on 2024-11-07 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reception_system", "0003_remove_seat_table_connect"),
    ]

    operations = [
        migrations.RenameField(
            model_name="seat",
            old_name="teble_number",
            new_name="table_number",
        ),
        migrations.RemoveField(
            model_name="seat",
            name="table_resevation",
        ),
        migrations.AddField(
            model_name="seat",
            name="table_connect",
            field=models.BooleanField(default=False, verbose_name="連結有、無"),
        ),
        migrations.AddField(
            model_name="seat",
            name="table_reservation",
            field=models.BooleanField(default=False, verbose_name="使用されているか"),
        ),
        migrations.AlterField(
            model_name="seat",
            name="clean",
            field=models.BooleanField(default=False, verbose_name="清掃済、未"),
        ),
        migrations.AlterField(
            model_name="seat",
            name="electrical_outlet",
            field=models.BooleanField(default=False, verbose_name="コンセント有、無"),
        ),
    ]
