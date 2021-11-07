# -*- coding: utf-8 -*-
# @Time    : 2021/11/6 21:40
# @Author  : JAKE4545
# @Email   : tmwu2018@163.com
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from settings import (
    MYSQL_DATABASE,
    MYSQL_HOST,
    MYSQL_PASSWORD,
    MYSQL_PORT,
    MYSQL_USER,
)

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()