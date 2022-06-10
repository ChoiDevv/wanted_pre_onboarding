from django.db import models


class Recruitments(models.Model):
    company = models.CharField(max_length=256, blank=False)
    country = models.CharField(max_length=20, blank=False)
    local = models.CharField(max_length=10, blank=False)
    recruit_content = models.TextField(blank=False)
    recruit_position = models.CharField(max_length=20, blank=False)
    recruit_compensation = models.IntegerField(blank=False)
    skill = models.CharField(max_length=10, blank=False)