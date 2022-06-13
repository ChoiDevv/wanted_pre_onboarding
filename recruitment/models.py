from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=20, blank=False)
    local = models.CharField(max_length=10, blank=False)


class Recruit(models.Model):
    position = models.CharField(max_length=20, blank=False)
    content = models.TextField(blank=False)
    skill = models.CharField(max_length=10, blank=False)
    recruit_compensation = models.IntegerField()