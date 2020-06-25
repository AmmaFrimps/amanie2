from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

phone_regex = RegexValidator(
    regex=r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$',
    message="Please enter a valid phone number.",
    code='invalid_phone_number')


class Queries(models.Model):
    query_email = models.CharField(_('query from'), max_length=30, blank=False)
    subject = models.CharField(_('subject'), max_length=40, blank=False)
    message = models.TextField(_('message'), blank=False)

    class Meta:
        ordering = ['-query_email']
        verbose_name = _('Query')
        verbose_name_plural = _('Queries')


class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False)
    work_id = models.CharField(max_length=30,
                               error_messages={'required': 'Please enter a valid  Identification Number(ID)'})
    rank = models.CharField(_('Rank'), max_length=30)
    location = models.CharField(_('Location'), max_length=30)

    can_access_dashboard = models.BooleanField(_('Can access dashboard'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['-last_name', '-first_name']
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return reverse('user_detail', args=[self.id])

    def get_email(self):
        return '%s' % self.email

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
