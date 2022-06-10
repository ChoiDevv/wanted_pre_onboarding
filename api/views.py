from rest_framework.generics import ListAPIView

from api.serializers import RecruitSerializer
from recruitment.models import Recruitment


class APIListView(ListAPIView):
    queryset = Recruitment.objects.all()
    serializer_class = RecruitSerializer

