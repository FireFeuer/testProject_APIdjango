from django.contrib import admin
from django.urls import path, include
from pages.views import CompanyListView
from pages.views import CompanyCreateAPIView
from pages.views import CompanyUpdateAPIView
from pages.views import CompanyDeleteAPIView
from rest_framework import routers




urlpatterns = [
    path('admin/', admin.site.urls),
    path('get/', CompanyListView.as_view(), name='company-list'),
    path('post/', CompanyCreateAPIView.as_view(), name='company-list'),
    path('put/<int:pk>/', CompanyUpdateAPIView.as_view(), name='company-list'),
    path('destroy/<int:id>/', CompanyDeleteAPIView.as_view(), name='company-list')

]
