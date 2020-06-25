from django.contrib import admin

from .models import Customer, PaymentRecord, Bin


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'area', 'zone', 'service_type')
    list_filter = ('first_name', 'last_name', 'area', 'zone', 'service_type', 'rate', 'phone_number')

    search_fields = ('first_name', 'last_name', 'house_no', 'service_type', 'rate',)
    ordering = ('last_name', 'first_name', 'phone_number')


@admin.register(PaymentRecord)
class PaymentRecordAdmin(admin.ModelAdmin):
    list_display = ('customer', 'collector', 'payment_period', 'amount_paid', 'payment_type')
    list_filter = ('customer', 'collector', 'payment_period', 'amount_paid',)

    search_fields = ('collector', 'payment_period', 'amount_paid',)


@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = ('customer', 'bin_id', 'level', 'code')
    list_filter = ('customer', 'bin_id', 'level',)

    search_fields = ('customer', 'bin_id', 'level',)
    ordering = ('customer', 'bin_id',)


admin.site.site_header = "Amanie"
