# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CevaShipmentDetail(models.Model):
    waybill_number = models.CharField(primary_key=True, max_length=100)
    ship_date = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.CharField(max_length=200, blank=True, null=True)
    estimated_delivery_date = models.CharField(max_length=100, blank=True, null=True)
    shipper_location = models.CharField(max_length=100, blank=True, null=True)
    consignee_location = models.CharField(max_length=100, blank=True, null=True)
    total_pcs = models.CharField(max_length=200, blank=True, null=True)
    actual_weight = models.CharField(max_length=1000, blank=True, null=True)
    charge_weight = models.CharField(max_length=200, blank=True, null=True)
    freight_terms = models.CharField(max_length=100, blank=True, null=True)
    service_level = models.CharField(max_length=100, blank=True, null=True)
    delivery_type = models.CharField(max_length=100, blank=True, null=True)
    movement_type = models.CharField(max_length=100, blank=True, null=True)
    history_data = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ceva_shipment_detail'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
