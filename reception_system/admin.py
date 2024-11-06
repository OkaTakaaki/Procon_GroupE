from django.contrib import admin
from .models import Reception, Seat, Join

#受付テーブル
admin.site.register(Reception)
#座席テーブル
admin.site.register(Seat)
#結合テーブル
admin.site.register(Join)