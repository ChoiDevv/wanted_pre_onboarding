from rest_framework.generics import ListAPIView, CreateAPIView

from api.serializers import RecruitListSerializer, RecruitCreateSerializer
from recruitment.models import Recruitments


class APIListView(ListAPIView):
    queryset = Recruitments.objects.all()
    serializer_class = RecruitListSerializer


class APICreateView(CreateAPIView):
    queryset = Recruitments.objects.all()
    serializer_class = RecruitCreateSerializer

