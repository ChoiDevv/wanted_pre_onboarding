from rest_framework import serializers

from recruitment.models import Recruitments


class RecruitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitments
        fields = ['id', 'company', 'country', 'local', 'recruit_position', 'recruit_compensation', 'skill']


class RecruitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitments
        fields = ['id', 'recruit_position', 'recruit_compensation', 'recruit_content', 'skill']

