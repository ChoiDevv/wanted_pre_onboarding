from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveAPIView

from api.serializers import CompanyListSerializer, RecruitCreateSerializer, RecruitDetailSerializer, \
    CompanyCreateSerializer
from recruitment.models import Recruit, Company


class CompanyListView(ListAPIView):
    queryset = Recruit.objects.all()
    serializer_class = CompanyListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['position', 'content', 'skill', 'recruit_compensation']


class RecruitCreateView(CreateAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitCreateSerializer


class RecruitDetailView(RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitDetailSerializer


class CompanyCreateView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateSerializer
