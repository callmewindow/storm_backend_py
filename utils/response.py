from django.http import *
import json
from django.core import serializers


def successRes(data=None, msg="操作成功"):
    res = HttpResponse(content_type='application/json')
    res.charset = 'UTF8'

    body = {}
    body['msg'] = msg
    body['data'] = serializers.serialize('json',data)
    body = json.dumps(body)
    print(body)
    print(type(body))
    # return JsonResponse(body, safe=True)
    return HttpResponse(body, content_type='application/json',charset='utf-8')


def failRes(msg="操作失败"):
    res = HttpResponse()
    res.charset = 'UTF-8'
    res.context = 'application/json'
    res.content = msg
    return HttpResponseBadRequest(res)


def notfoundRes(msg="未找到资源"):
    res = HttpResponse()
    res.charset = 'UTF-8'
    res.context = 'application/json'
    body = {msg}
    res.content = body
    return HttpResponseNotFound(res)