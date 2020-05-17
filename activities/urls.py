from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('detail/<int:activity_id>/', views.detail, name = 'detail'),
    path('exclude/<int:activity_id>/', views.exclude, name = 'exclude'),
]