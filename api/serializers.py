from rest_framework import serializers

from recruitment.models import Recruitment


class RecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'

