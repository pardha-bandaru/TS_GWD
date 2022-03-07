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
        return JsonResponse({"a": "b"})
    return HttpResponse("Hello, world. You're at the polls index.")


def get_districts_list(request: Request):
    districts_response = get_districts_list_impl(request)
    return JsonResponse(districts_response)


def get_mandals_list(request: Request, district_name: str):
    mandals_list = get_mandals_list_impl(district_name)
    return JsonResponse(mandals_list)


def get_water_levels(request: Request, district_name, mandal_name):
    mandal_waterlevel_info = get_water_levels_impl(mandal_name)
    return JsonResponse(mandal_waterlevel_info)


def get_water_quality(request: Request, district_name, mandal_name):
    mandal_water_quality_info = get_water_quality_impl(mandal_name)
    return JsonResponse(mandal_water_quality_info)


def get_districts_list_impl(request):
    districts = list(GW_General.objects.values_list("District"))
    districts = list(set([disctrict[0] for disctrict in districts]))
    response = {
        "status": "SUCCESS",
        "status_code": 200,
        "results": {"districts": districts},
    }
    return response


def get_mandals_list_impl(district_name):
    mandals = list(
        GW_General.objects.filter(District="Adilabad").values_list("GP_Mandal")
    )
    mandals = list(set([mandal[0] for mandal in set(mandals)]))
    response = {
        "status": "SUCCESS",
        "status_code": 200,
        "results": {"district": district_name, "mandals": mandals},
    }
    return response


def get_water_levels_impl(mandal_name):
    mandal_wells_list = GW_General.objects.filter(GP_Mandal=mandal_name).values_list(
        "WellNo"
    )
    mandal_wells_list = list(set([mandal_well[0] for mandal_well in mandal_wells_list]))
    mandal_water_level = {}
    for well_id in mandal_wells_list:
        mandal_water_level[well_id] = []
        for water_level_detail in WaterLevels.objects.filter(WellNo=well_id):
            water_level_detail_dict = {
                    "date": water_level_detail.date,
                    "time": water_level_detail.time,
                    "Water_Level": water_level_detail.Water_Level,
                    "Water_Level_MBMP": water_level_detail.Water_Level_MBMP,
                }
            mandal_water_level[well_id].append(water_level_detail_dict)
    response = {
        "status": "SUCCESS",
        "status_code": 200,
        "results": {"mandal": mandal_name, "mandal_water_info": mandal_water_level},
    }
    return response


def get_water_quality_impl(mandal_name):
    mandal_wells_list = GW_General.objects.filter(GP_Mandal=mandal_name).values_list(
        "WellNo"
    )
    mandal_wells_list = list(set([mandal_well[0] for mandal_well in mandal_wells_list]))
    mandal_water_quality = {}
    for well_id in mandal_wells_list:
        mandal_water_quality[well_id] = []

        for water_quality_detail in WaterQuality.objects.filter(WellNo=well_id):
            water_quality_detail_dict = {
                "SampleID": water_quality_detail.SampleID,
                "SamplingDate": water_quality_detail.SamplingDate,
                "pH": water_quality_detail.pH,
                "EC": water_quality_detail.EC,
                "THard": water_quality_detail.THard,
                "TDS": water_quality_detail.TDS,
                "CO3": water_quality_detail.CO3,
                "HCO3": water_quality_detail.HCO3,
                "Cl": water_quality_detail.Cl,
                "SO4": water_quality_detail.SO4,
                "NO3": water_quality_detail.NO3,
                "Ca": water_quality_detail.Ca,
                "Mg": water_quality_detail.Mg,
                "Na": water_quality_detail.Na,
                "K": water_quality_detail.K,
                "F": water_quality_detail.F,
            }
            mandal_water_quality[well_id].append(water_quality_detail_dict)
    response = {
        "status": "SUCCESS",
        "status_code": 200,
        "results": {"mandal": mandal_name, "mandal_water_info": mandal_water_quality},
    }
    return response
