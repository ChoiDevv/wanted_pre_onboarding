from django.urls import include, path

from api import views


api_name = 'api'
urlpatterns = [
    path('list/', views.APIListView.as_view(), name="list"),
    path('create/', views.APICreateView.as_view(), name="create"),
    path('<int:pk>/update/', views.APIUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.APIDeleteView.as_view(), name="delete"),
]