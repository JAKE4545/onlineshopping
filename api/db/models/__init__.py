# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 22:03
# @Author  : JAKE4545
# @Email   : tmwu2018@163.com

import ormar
import sqlalchemy
import databases

from settings import (
    MYSQL_DATABASE,
    MYSQL_HOST,
    MYSQL_PASSWORD,
    MYSQL_PORT,
    MYSQL_USER,
)

DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database