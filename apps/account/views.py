
from django.shortcuts import render

import datetime
import traceback

from django.forms.models import model_to_dict
from django.http.response import HttpResponse

from models.Account import *
# from bot.models import Bot as BotCon
from utils.response import *


def json_raw(dict):
    return str(dict).replace('\'', '\"').replace('None', 'null')


def model_to_dict_fixed(model):
    d = model_to_dict(model)
    for key in d.keys():
        if d[key].__class__ == datetime.datetime:
            d[key] = d[key].strftime('%Y-%m-%d %H:%M:%S')
    return d


def api_format(request):
    try:
        dict = request.POST
        msg = {}


    except:
        traceback.print_exc()
        msg['result'] = 'Unexpected Error'
        return HttpResponse(json_raw(msg))

# 注册
def register(request):
    try:
        dict = request.POST

        account = Account()
        account.username = dict.get('username', None)
        account.password = dict.get('password', None)
        if account.username in [None, ''] or account.password in ['', None]:
            return failRes('用户名或密码不能为空')
        elif Account.objects.filter(username=account.username):
            return failRes('用户名重复')
        account.save()
        return successRes(None,'注册成功')
    except Exception:
        traceback.print_exc()
        return HttpResponseServerError(Exception)

# 登录
def login(request):
    try:
        dict = request.POST

        username = dict.get('username', None)
        password = dict.get('password', None)
        if username in [None, ''] or password in ['', None]:
            return failRes('用户名或密码不能为空')

        find = Account.objects.filter(username=username, password=password)
        if find:
            return successRes(find, "登录成功")
        else:
            return failRes('用户名或密码错误')

    except Exception:
        traceback.print_exc()
        return HttpResponseServerError(Exception)

# 用户信息
def info(request, user_id):
    try:
        # dict = request.GET

        if user_id is None:
            return failRes('用户ID不能为空')

        # find = Account.objects.get(id=user_id)
        # 如果选择了部分value，则会犹豫返回的值不是一个list，而是一个dict，导致无法序列化
        find = Account.objects.filter(id__gt=0)
        # find = serializers.serialize('json',find)
        print(find[0].description)
        if find:
            # return successRes(model_to_dict_fixed(find))
            # return render(request, '' {'find': find})
            return successRes(find)
        else:
            return failRes('不存在对应id的用户')
    except:
        traceback.print_exc()
        return HttpResponseServerError(Exception)
