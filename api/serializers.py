from rest_framework import serializers

from recruitment.models import Recruit, Company


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        fields = '__all__'


class RecruitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        fields = '__all__'


class RecruitDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        fields = '__all__'


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

