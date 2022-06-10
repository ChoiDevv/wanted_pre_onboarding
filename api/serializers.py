from rest_framework import serializers

from recruitment.models import Recruitments


class RecruitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitments
        exclude = ['recruit_content']


class RecruitPersonalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitments
        fields = '__all__'

