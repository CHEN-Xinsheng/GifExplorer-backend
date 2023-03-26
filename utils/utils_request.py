'''
    This utils_request.py file contains tools to generate http response
'''
from django.http import JsonResponse


def request_failed(code, info, status_code=400, data={}):
    '''
        Return a http failure response
    '''
    return JsonResponse({
        "code": code,
        "info": info,
        **data
    }, status=status_code)


def request_success(data={}):
    '''
        Return a http success response
    '''
    return JsonResponse({
        "code": 0,
        "info": "Succeed",
        **data
    })


def return_field(obj_dict, field_list):
    '''
        Return specific key-value pairs
    '''
    for field in field_list:
        assert field in obj_dict, f"Field `{field}` not found in object."

    return {
        k: v for k, v in obj_dict.items()
        if k in field_list
    }

BAD_METHOD = request_failed(-3, "Bad method", 405, {"data": {}})

NOT_FOUND = request_failed(1000, "NOT_FOUND", 404, {"data": {}})
