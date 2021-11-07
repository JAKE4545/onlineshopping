# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 21:07
# @Author  : JAKE4545
# @Email   : tmwu2018@163.com
from pydantic import BaseModel

class UserWithToken(BaseModel):
    id: str
    username: str
    token: str

class UserForm(BaseModel):
    username: str
    password: str