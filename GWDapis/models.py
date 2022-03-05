from django.conf import settings
from django.db import models
from django.utils import timezone


class GW_General(models.Model):
    WellNo = models.CharField(max_length=10, blank=True, null=True)
    Well_Type = models.CharField(max_length=18, blank=True, null=True)
    Agency = models.CharField(max_length=5, blank=True, null=True)
    State = models.CharField(max_length=9, blank=True, null=True)
    District = models.CharField(max_length=23, blank=True, null=True)
    Block_Taluk = models.CharField(max_length=20, blank=True, null=True)
    GP_Mandal = models.CharField(max_length=25, blank=True, null=True)
    Village = models.CharField(max_length=25, blank=True, null=True)
    Basin = models.CharField(max_length=8, blank=True, null=True)
    Minor_Basin = models.CharField(max_length=15, blank=True, null=True)
    Geology = models.CharField(max_length=28, blank=True, null=True)
    Geomorphology = models.CharField(max_length=19, blank=True, null=True)
    Easting = models.DecimalField(max_digits=8,decimal_places=2, blank=True, null=True)
    Northing = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Command_Area = models.CharField(max_length=5, blank=True, null=True)
    MP = models.CharField(max_length=1, blank=True, null=True)
    DWLR_installed = models.CharField(max_length=5, blank=True, null=True)
    dwlr_no = models.CharField(max_length=8, blank=True, null=True)
    DWLR_type = models.CharField(max_length=1, blank=True, null=True)
    Category = models.CharField(max_length=10, blank=True, null=True)


class WaterLevels(models.Model):
    WellNo = models.CharField(max_length=10, blank=True, null=True)
    date = models.CharField(max_length=19, blank=True, null=True)
    time = models.CharField(max_length=19, blank=True, null=True)
    Water_Level = models.DecimalField(max_digits=8,decimal_places=2, blank=True, null=True)
    Water_Level_MBMP = models.DecimalField(max_digits=8,decimal_places=2, blank=True, null=True)


class WaterQuality(models.Model):
    WellNo  = models.CharField(max_length=10, blank=True, null=True)
    SampleID  = models.IntegerField(blank=True, null=True)
    SamplingDate  = models.CharField(max_length=19, blank=True, null=True)
    pH  = models.CharField(max_length=7, blank=True, null=True)
    EC  = models.CharField(max_length=5, blank=True, null=True)
    THard  = models.CharField(max_length=8, blank=True, null=True)
    TDS  = models.CharField(max_length=7, blank=True, null=True)
    CO3  = models.CharField(max_length=6, blank=True, null=True)
    HCO3  = models.CharField(max_length=8, blank=True, null=True)
    Cl  = models.CharField(max_length=8, blank=True, null=True)
    SO4  = models.CharField(max_length=6, blank=True, null=True)
    NO3  = models.CharField(max_length=10, blank=True, null=True)
    Ca  = models.CharField(max_length=8, blank=True, null=True)
    Mg  = models.CharField(max_length=9, blank=True, null=True)
    Na  = models.CharField(max_length=8, blank=True, null=True)
    K  = models.CharField(max_length=8, blank=True, null=True)
    F  = models.CharField(max_length=6, blank=True, null=True)
