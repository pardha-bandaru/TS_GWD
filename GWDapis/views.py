import re
from urllib import response
from urllib.request import Request
from django.shortcuts import render


from django.http import HttpResponse, JsonResponse
from django.core import serializers

import GWDapis
from utils.session_decorators import require_valid_session
from .models import GW_General, WaterLevels, WaterQuality, Wells, WellDepth


def index(request: Request):
    if request.method == "POST":
        gw_obj = GW_General(**request.POST.dict())
        # gw_obj.save()
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
        "WellNo", "Northing", "Easting"
    )
    mandal_wells_list = list(set([(mandal_well[0], float(mandal_well[1]), float(mandal_well[2])) for mandal_well in mandal_wells_list]))
    mandal_water_level = {}
    for well_id, latitude, longitude in mandal_wells_list:
        mandal_water_level[well_id] = []
        # for water_level_detail in WaterLevels.objects.filter(WellNo=well_id):
        water_level_detail = WaterLevels.objects.filter(WellNo=well_id).last()
        water_level_detail_dict = {
                "date": water_level_detail.date,
                "time": water_level_detail.time,
                "Water_Level": water_level_detail.Water_Level,
                "location": {
                    "latitude": float(latitude),
                    "longitude": float(longitude)
                },
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
        "WellNo", "Northing", "Easting"
    )
    mandal_wells_list = list(set([(mandal_well[0], float(mandal_well[1]), float(mandal_well[2])) for mandal_well in mandal_wells_list]))
    mandal_water_quality = {}
    for well_id, latitude, longitude in mandal_wells_list:
        mandal_water_quality[well_id] = []
        water_quality_detail = WaterQuality.objects.filter(WellNo=well_id).last()
        water_quality_detail_dict = {
            "SampleID": water_quality_detail.SampleID,
            "SamplingDate": water_quality_detail.SamplingDate,
            "location": {
                    "latitude": float(latitude),
                    "longitude": float(longitude)
                },
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


def register_mobile(request):
    if request.GET.get('clientKey') or request.POST.get('clientKey'):
        return JsonResponse({'status':'FAILED','message':"device already registered"}, status=500)
    else:
        session_key = request.session._get_or_create_session_key()
        request.session['clientKey'] = session_key
        response = {
            "status": "SUCCESS",
            "status_code": 200,
            "sessionKey":session_key
        }
        return JsonResponse(response)


@require_valid_session
def my_well(request: Request, session):
    if request.method == "POST":
        post_data = request.POST.dict()
        water_depth = post_data.pop("water_depth", None)
        wells_obj = Wells(**request.POST.dict(), session_id=session)
        wells_obj.save()
        if water_depth:
            water_depth_obj = WellDepth(registration_number=wells_obj, water_depth=water_depth)
            water_depth_obj.save()
        return JsonResponse({"status": "SUCCESS", "status_code": 201, "message":"Succesfully saved well data"}, status=201)
    
    if request.method == "PUT":
        if hasattr(request, '_post'):
            del request._post
            del request._files
        
        try:
            request.method = "POST"
            request._load_post_and_files()
            #body = request.body
            request.method = "PUT"
        except AttributeError:
            request.META['REQUEST_METHOD'] = 'POST'
            request._load_post_and_files()
            request.META['REQUEST_METHOD'] = 'PUT'
            
        request.PUT = request.POST
        try:
            post_data = request.POST.dict()
            water_depth = post_data.pop("water_depth")
            registration_number = post_data.pop("registration_number")
            wells_obj = Wells.objects.get(registration_number=registration_number)
            if water_depth:
                water_depth_obj = WellDepth(registration_number=wells_obj, water_depth=water_depth)
                water_depth_obj.save()
                return JsonResponse({"status": "SUCCESS", "status_code": 201, "message":"Succesfully saved well data"}, status=201)
        except Exception as e:
            print(e)
            return JsonResponse({"status": "FAILED", "status_code": 422, "message":"Failed to update well data Missing required fields"}, status=201)

    
    my_well_objs = Wells.objects.filter(session_id=session)
    my_well_result = []
    for my_well_obj in my_well_objs:
        my_well_data = {
            "registration_number": my_well_obj.registration_number,
            "phone_number": my_well_obj.phone_number,
            "longitude": float(my_well_obj.longitude),
            "latitude": float(my_well_obj.latitude),
            "type_of_well": my_well_obj.type_of_well,
            "total_depth": float(my_well_obj.total_depth),
            "created_at" : str(my_well_obj.created_at),
            "measurements": []
        }
        for welldepth_mesurment in WellDepth.objects.filter(registration_number=my_well_obj):
            my_well_data["measurements"].append({
                "well_depth": float(welldepth_mesurment.water_depth),
                "measured_at": str(welldepth_mesurment.created_at)
            })
        my_well_result.append(my_well_data)
    
    response = {
        "status": "SUCCESS",
        "status_code": 200,
        "results": {"myWell": my_well_result}
    }
    return JsonResponse(response)
