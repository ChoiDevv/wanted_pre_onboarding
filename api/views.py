from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CompanyRecruitSerializer, TestSerializer
from recruitment.models import Recruit, Company, Test


class CompanyCreatedRecruitView(ListAPIView):
    queryset = Recruit.objects.all()
    serializer_class = CompanyRecruitSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['position', 'content', 'skill', 'recruit_compensation']


class CompanyCreateAPIView(CreateAPIView):
    queryset = Recruit.objects.all()
    serializer_class = CompanyRecruitSerializer


class DifferentCreatedRecruitView(RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView):
    queryset = Recruit.objects.all()
    serializer_class = CompanyRecruitSerializer
