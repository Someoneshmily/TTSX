# coding=utf-8
from django.db import models

# Create your models here.


class UserInfo(models.Model):

    uname = models.CharField(max_length=20)
    upub = models.CharField(max_length=40)  # sha1
    umail = models.CharField(max_length=30)
    urecieve = models.CharField(max_length=20)  # 接收人
    uaddress = models.CharField(max_length=100)  # 地址
    ucode = models.CharField(max_length=6)  # 编码
    uphone = models.CharField(max_length=11)  # 机号