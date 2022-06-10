from django.urls import path

from api import views


api_name = 'api'
urlpatterns = [
    path('list/', views.APIListView.as_view(), name="list"),
    path('list/<int:pk>/', views.APIPersonalView.as_view(), name="personal-list"),
    path('create/', views.APICreateView.as_view(), name="create"),
]

