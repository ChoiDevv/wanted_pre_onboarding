from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=50, blank=False, null=True)
    country = models.CharField(max_length=20, blank=False, null=True)
    local = models.CharField(max_length=10, blank=False, null=True)


class Recruit(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, blank=False)
    content = models.TextField(blank=False)
    skill = models.CharField(max_length=10, blank=False)
    recruit_compensation = models.IntegerField()

