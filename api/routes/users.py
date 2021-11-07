# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 20:55
# @Author  : JAKE4545
# @Email   : tmwu2018@163.com
from fastapi import FastAPI

user_api = FastAPI(description="用户模块的相关内容编写")

user_api.post("meiduo_admin/authorizations/")
async def login():
    pass