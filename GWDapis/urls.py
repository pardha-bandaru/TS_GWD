from django.urls import path

from . import views

urlpatterns = [
    path('uploadGW_General', views.index, name='index'),
    path('districts/', views.get_districts_list, name='get_districts_list'),
    # path('districts/<str:district_id>', views.get_districts_details, name='get_districts_details'),
    path('districts/<str:district_name>/mandals/', views.get_mandals_list, name='get_mandals_list'),
    # path('districts/<str:district_id>/mandals/<str:mandal_id>', views.get_mandals_details, name='get_mandals_details'),
    path('districts/<str:district_name>/mandals/<str:mandal_name>/waterLevels', views.get_water_levels, name='get_water_levels'),
    path('districts/<str:district_name>/mandals/<str:mandal_name>/waterQuality', views.get_water_quality, name='get_water_quality'),
]