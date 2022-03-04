from urllib import response
from urllib.request import Request
from django.shortcuts import render



from django.http import HttpResponse, JsonResponse
from django.core import serializers

import GWDapis
from .models import GW_General, WaterLevels, WaterQuality


def index(request: Request):
    if request.method == "POST":
        gw_obj = GW_General(**request.POST.dict())
        gw_obj.save()
        return JsonResponse({"a":"b"})
    return HttpResponse("Hello, world. You're at the polls index.")



def get_districts_list(request:Request):
    districts_response = get_districts_list_impl(request)
    return JsonResponse(districts_response)

def get_mandals_list(request:Request, district_name:str):
    mandals_list = get_mandals_list_impl(district_name)
    return JsonResponse(mandals_list)

def get_water_levels(request: Request, mandal_name):
    mandal_waterlevel_info = get_water_levels_impl(mandal_name)
    return JsonResponse(mandal_waterlevel_info)

def get_water_quality(request: Request, mandal_name):
    mandal_water_quality_info = get_water_quality_impl(mandal_name)
    return JsonResponse(mandal_water_quality_info)


def get_districts_list_impl(request):
    districts = list(GW_General.objects.values_list('District'))
    districts = list(set([disctrict[0] for disctrict in districts]))
    response = {
        "status": "SUCCESS",
        "status_code":200, 
        "results": {
            "districts": districts
            }
        }
    return response

def get_mandals_list_impl(district_name):
    mandals = list(GW_General.objects.filter(District='Adilabad').values_list('GP_Mandal'))
    mandals = list(set([mandal[0] for mandal in set(mandals)]))
    response = {
        "status": "SUCCESS",
        "status_code":200, 
        "results": {
            "district": district_name,
            "mandals": mandals
        }
    }
    return response


def get_water_levels_impl(mandal_name):
    mandal_wells_list = GW_General.objects.filter(GP_Mandal=mandal_name).values_list('WellNo')
    mandal_wells_list = list(set([mandal_well[0] for mandal_well in mandal_wells_list]))
    mandal_water_level = {}
    for well_id in mandal_wells_list:
        water_level_details = WaterLevels.objects.filter(WellNo=well_id).last()
        mandal_water_level[well_id] = {
            "WL_Well_Depth": water_level_details.WL_Well_Depth,
            "Water_Level" : water_level_details.Water_Level,
        }
    response = {
        "status": "SUCCESS",
        "status_code":200, 
        "results": {
            "mandal": mandal_name,
            "mandal_water_info": mandal_water_level
        }
    }
    return response

def get_water_quality_impl(mandal_name):
    mandal_wells_list = GW_General.objects.filter(GP_Mandal=mandal_name).values_list('WellNo')
    mandal_wells_list = list(set([mandal_well[0] for mandal_well in mandal_wells_list]))
    mandal_water_quality = {}
    for well_id in mandal_wells_list:
        water_quality_details = WaterQuality.objects.filter(WellNo=well_id).last()
        mandal_water_quality[well_id] = {
            "SampleID": water_quality_details.SampleID,
            "pH" : water_quality_details.pH,
            "EC" : water_quality_details.EC,
            "THard" : water_quality_details.THard,
            "TDS": water_quality_details.TDS,
        }
    response = {
        "status": "SUCCESS",
        "status_code":200, 
        "results": {
            "mandal": mandal_name,
            "mandal_water_info": mandal_water_quality
        }
    }
    return response