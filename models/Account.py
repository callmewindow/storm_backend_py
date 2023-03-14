from django.db import models
from django.utils.timezone import now


class Account(models.Model):
    username = models.CharField('用户名', unique=True, max_length=100)
    password = models.CharField('密码', max_length=100)
    nickname = models.CharField('昵称', max_length=20)
    email = models.CharField('邮箱', max_length=50)
    avatar = models.CharField('头像', max_length=300)
    identity = models.IntegerField('身份', blank=False, null=False, default=0)
    description = models.TextField('描述', null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        # 注意指定app名称
        app_label = 'account'
        db_table = 'account'