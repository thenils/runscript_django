
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.StudentListView.as_view(), name="home"),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='detail'),
]
