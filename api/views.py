from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveAPIView

from api.serializers import RecruitListSerializer, RecruitPersonalListSerializer
from recruitment.models import Recruitments


class APIListView(ListAPIView):
    queryset = Recruitments.objects.all()
    serializer_class = RecruitListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['company', 'recruit_position', 'skill']


class APICreateView(CreateAPIView):
    queryset = Recruitments.objects.all()
    serializer_class = RecruitListSerializer


class APIPersonalView(RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView):
    queryset = Recruitments.objects.all()
    serializer_class = RecruitPersonalListSerializer



