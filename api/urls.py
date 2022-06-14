from django.urls import path

from api import views


api_name = 'api'
urlpatterns = [
    path('create/', views.RecruitCreateView.as_view(), name="create"),
    path('list/', views.CompanyListView.as_view(), name="list"),
    path('list/<int:pk>/', views.RecruitDetailView.as_view(), name="personal-list"),
    path('company/', views.CompanyCreateView.as_view(), name="company"),
]
