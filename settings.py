# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 21:04
# @Author  : JAKE4545
# @Email   : tmwu2018@163.com
import os

# Database
MYSQL_HOST = os.environ.get("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "onlineshopping")
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_DATABASE", "123456")

# jwt
SECRET_KEY = "09d35e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30