from django.http import JsonResponse


def require_valid_session(view_function):
    def decorated(request, *args, **kwargs):
        if request.session.get("clientKey"):
            return view_function(request, request.session['clientKey'], *args, **kwargs)
        else:
            return JsonResponse({'status':'FAILED','message':"Invalid Session register the app"}, status=500)
    return decorated
