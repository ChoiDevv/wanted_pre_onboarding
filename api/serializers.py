from rest_framework import serializers

from recruitment.models import Recruit


class CompanyRecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        fields = '__all__'


class RecruitPersonalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        fields = '__all__'