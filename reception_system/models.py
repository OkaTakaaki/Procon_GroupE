from django.db import models

#座席テーブル
from django.db import models

class Seat(models.Model):
    seat_id = models.AutoField(primary_key=True)  
    table_number = models.IntegerField(verbose_name="テーブル番号")
    table_resevation = models.BooleanField(verbose_name="使用されているか", default=False)  # 使用されているか
    recommended_capacity = models.IntegerField(verbose_name="座席人数", null=False)
    table_type = models.IntegerField(verbose_name="座席種別", null=False)
    electrical_outlet = models.BooleanField(verbose_name="コンセント有、無", default=False)  # コンセント有無
    clean = models.BooleanField(verbose_name="清掃済、未", default=False)  # 清掃済か未か
    table_connect = models.BooleanField(verbose_name="連結有、無", default=False)  # 連結有無

    def __str__(self):
        return f"Seat {self.table_number} ({self.table_type})"


#受付テーブル
class Reception(models.Model):
    reception_number = models.CharField(max_length=10, verbose_name="受付番号")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, null=True, blank=True)
    payment_status = models.BooleanField(verbose_name="会計状況", null=False, default=False)
    reception_count = models.IntegerField(verbose_name="利用人数", null=False, blank=True)
    conditions = models.CharField(verbose_name="条件", null=True, max_length=100, blank=True)
    reception_time = models.DateTimeField(verbose_name="利用開始時間", null=True, blank=True)

#結合テーブル
class Join(models.Model):
    join_source = models.CharField(verbose_name="結合元", null=False, max_length=50)
    join_target = models.CharField(verbose_name="結合先", null=False, max_length=50)
    