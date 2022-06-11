from django.urls import path

from api import views


api_name = 'api'
urlpatterns = [
    path('create/', views.CompanyCreateAPIView.as_view(), name="create"),
    path('list/', views.CompanyCreatedRecruitView.as_view(), name="list"),
    path('list/<int:pk>/', views.DifferentCreatedRecruitView.as_view(), name="personal-list"),
]
