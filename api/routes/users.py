# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 20:55
# @Author  : JAKE4545
# @Email   : tmwu2018@163.com
from fastapi import FastAPI,Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from api.exts.jwt import jwt_response_payload_handler

from ..schemas import UserForm
from api.db.models.users import User

user_api = FastAPI(description="用户模块的相关内容编写")

user_api.post("meiduo_admin/authorizations/")
async def login(username: str, password: str):
    # 先查询数据
    curr_user = User.objects.get_or_none(username=username)
    if
