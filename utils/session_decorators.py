from django.http import JsonResponse


def require_valid_session(view_function):
    def decorated(request, *args, **kwargs):
        client_key = None
        if request.GET.get("clientKey"):
            client_key = request.GET.get("clientKey")
        elif request.session.get("clientKey"):
            client_key = request.session.get("clientKey")
        if client_key:
            return view_function(request, client_key, *args, **kwargs)
        else:
            return JsonResponse({'status':'FAILED','message':"Invalid Session register the app"}, status=500)
    return decorated
