from django.db import models

class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)

    # 联系电话
    phonenumber = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)

    # qq
    qq  = models.CharField(max_length=30,null=True,blank=True)


from django.contrib import admin
admin.site.register(Customer)
