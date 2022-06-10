from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from api.serializers import RecruitListSerializer
from recruitment.models import Recruitments


class APIListView(ListAPIView):
    queryset = Recruitments.objects.all()
    serializer_class = RecruitListSerializer


class APICreateView(CreateAPIView):
    queryset = Recruitments.objects.all()
    serializer_class = RecruitListSerializer


class APIUpdateView(RetrieveUpdateAPIView):
    queryset = Recruitments.objects.all()
    serializer_class = RecruitListSerializer


class APIDeleteView(RetrieveDestroyAPIView):
    queryset = Recruitments.objects.all()
    serializer_class = RecruitListSerializer

