from django.db import models

#座席テーブル
class Seat(models.Model):
    teble_number = models.IntegerField(verbose_name="テーブル番号", null=False)
    table_resevation = models.BooleanField(verbose_name="使用されているか", null=False)
    recommended_capacity = models.IntegerField(verbose_name="座席人数", null=False)
    table_type = models.IntegerField(verbose_name="座席種別", null=False)
    electrical_outlet = models.BooleanField(verbose_name="コンセント有、無", null=True)
    clean = models.BooleanField(verbose_name="清掃済、未", null=True)

#受付テーブル
class Reception(models.Model):
    reception_number = models.AutoField(primary_key=True, verbose_name="受付番号", null=False)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    payment_status = models.BooleanField(verbose_name="会計状況", null=False)
    reception_count = models.IntegerField(verbose_name="利用人数", null=False)
    conditions = models.CharField(verbose_name="条件", null=True, max_length=100)
    reception_time = models.DateTimeField(verbose_name="利用開始時間", null=True)

#結合テーブル
class Join(models.Model):
    join_source = models.CharField(verbose_name="結合元", null=False, max_length=50)
    join_target = models.CharField(verbose_name="結合先", null=False, max_length=50)
    