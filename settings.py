# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 21:04
# @Author  : JAKE4545
# @Email   : tmwu2018@163.com
import os

MYSQL_HOST = os.environ.get("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3307))
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "onlineshopping")
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_DATABASE", "123456")