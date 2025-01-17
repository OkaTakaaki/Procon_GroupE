# Generated by Django 5.1.2 on 2025-01-17 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_source', models.CharField(max_length=50, verbose_name='結合元')),
                ('join_target', models.CharField(max_length=50, verbose_name='結合先')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(unique=True, verbose_name='テーブル番号')),
                ('table_resevation', models.BooleanField(default=False, verbose_name='使用されているか')),
                ('recommended_capacity', models.IntegerField(verbose_name='座席人数')),
                ('table_type', models.IntegerField(verbose_name='座席種別')),
                ('electrical_outlet', models.BooleanField(default=False, verbose_name='コンセント有、無')),
                ('clean_status', models.BooleanField(default=False, verbose_name='清掃済、未')),
                ('table_connect', models.BooleanField(default=False, verbose_name='連結有、無')),
            ],
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('reception_number', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='受付番号')),
                ('payment_status', models.BooleanField(default=False, verbose_name='会計状況')),
                ('reception_count', models.IntegerField(blank=True, verbose_name='利用人数')),
                ('table_type', models.IntegerField(default=0, verbose_name='座席種別')),
                ('electrical_outlet', models.BooleanField(default=False, verbose_name='コンセント有、無')),
                ('table_connect', models.BooleanField(default=False, verbose_name='連結有、無')),
                ('reception_time', models.DateTimeField(blank=True, null=True, verbose_name='利用開始時間')),
                ('seat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reception_system.seat')),
            ],
        ),
    ]
