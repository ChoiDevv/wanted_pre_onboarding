from django.contrib import admin

from recruitment.models import Recruit, Company

admin.site.register(Company)
admin.site.register(Recruit)