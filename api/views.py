from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, \
    RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ListSerializer, RecruitCreateSerializer, RecruitDetailSerializer, \
    CompanyCreateSerializer
from recruitment.models import Recruit, Company


class CompanyListView(APIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['position', 'content', 'skill', 'recruit_compensation']
    def get(self, request, *args, **kwargs):
        company = Company.objects.all()
        recruit = Recruit.objects.all()

        data = {
            'company': company,
            'recruit': recruit,
        }

        serializer = ListSerializer(instance=data)
        return Response(serializer.data)



class RecruitCreateView(CreateAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitCreateSerializer


class RecruitDetailView(RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitDetailSerializer


class CompanyCreateView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateSerializer
