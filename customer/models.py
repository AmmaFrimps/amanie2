from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from authentication.models import User

# Create your models here.
phone_regex = RegexValidator(
    regex=r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$',
    message="Please enter a valid phone number.",
    code='invalid_phone_number')


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    zone = models.CharField(max_length=30)
    house_no = models.CharField(max_length=30)
    service_type = models.CharField(max_length=30)
    rate = models.CharField(max_length=30)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False)

    class Meta:
        ordering = ['-last_name']
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Bin(models.Model):
    customer = models.ForeignKey(Customer, related_name="bin", on_delete=models.CASCADE)
    bin_id = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    code = models.CharField(max_length=30)

    class Meta:
        ordering = ['-bin_id']
        verbose_name = _('Bin')
        verbose_name_plural = _('Bins')

    def __str__(self):
        return '%s' % self.bin_id


class PaymentRecord(models.Model):
    PAYMENT_INTERVAL = (
        ('per_pickup', 'Per Pick-Up'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    )

    PAYMENT_TYPE = (
        ('mobile_money', 'Mobile Money'),
        ('cash', 'Cash'),
    )

    customer = models.ForeignKey(Customer, related_name="payment_record", on_delete=models.CASCADE)
    payment_period = models.CharField(max_length=10, choices=PAYMENT_INTERVAL, default="period")
    amount_paid = models.IntegerField(default=15)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE, default="payment_period")
    collector = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True,
                                  related_name='collector_name')
    date_of_payment = models.DateTimeField(auto_now=True)
    remarks = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % self.payment_period

    class Meta:
        ordering = ['-payment_period']
        verbose_name = _('Payment Record')
        verbose_name_plural = _('Payment Records')
