from django.db import models

class Bank(models.Model):
    ifsc = models.CharField(max_length=11, blank=False, default='')
    bank_id = models.BigIntegerField(blank=False, default='')
    branch = models.CharField(max_length=74, blank=False, default='')
    address = models.CharField(max_length=195, blank=False, default='')
    city = models.CharField(max_length=50, blank=False, default='')
    district = models.CharField(max_length=50, blank=False, default='')
    state = models.CharField(max_length=26, blank=False, default='')
    bank_name = models.CharField(max_length=50, blank=False, default='')
