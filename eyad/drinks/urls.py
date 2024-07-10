  

from django.contrib import admin
from django.urls import path
from drinks import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('drinks/', views.drink_list),
    path('drinks/<int:id>', views.drink_detail)
]