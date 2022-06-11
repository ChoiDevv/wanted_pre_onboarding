from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveAPIView

from api.serializers import CompanyRecruitSerializer, RecruitPersonalListSerializer
from recruitment.models import Recruit, Company


class CompanyCreatedRecruitView(ListAPIView):
    queryset = Recruit.objects.all()
    serializer_class = CompanyRecruitSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['company', 'position', 'skill']


class CompanyCreateAPIView(CreateAPIView):
    queryset = Recruit.objects.all()
    serializer_class = CompanyRecruitSerializer


class DifferentCreatedRecruitView(RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView):
    queryset = Recruit.objects.all()
    serializer_class = CompanyRecruitSerializer

