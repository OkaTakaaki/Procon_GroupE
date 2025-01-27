from django.contrib import admin
from .models import Reception, Seat, Join

class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('reception_number', 'reception_count', 'get_table_type_display', 'electrical_outlet', 'table_connect', 'reception_time')

    def get_table_type_display(self, obj):
        return obj.get_table_type_display()
    get_table_type_display.short_description = 'Table Type'

class SeatAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'recommended_capacity', 'get_table_type_display', 'table_resevation', 'electrical_outlet', 'clean_status', 'table_connect')

    def get_table_type_display(self, obj):
        return obj.get_table_type_display()
    get_table_type_display.short_description = 'Table Type'



#受付テーブル
admin.site.register(Reception,ReceptionAdmin)
#座席テーブル
admin.site.register(Seat, SeatAdmin)
#結合テーブル
admin.site.register(Join)