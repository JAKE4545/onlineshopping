# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 22:03
# @Author  : JAKE4545
# @Email   : tmwu2018@163.com
import ormar
import sqlalchemy
import asyncio

from base import BaseMeta, DATABASE_URL, database, metadata


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=20, unique=True)
    email: str = ormar.String(max_length=30, unique=True)
    password: str = ormar.String(max_length=255)
    mobile: str = ormar.String(max_length=12, unique=True)
    user_level: int = ormar.SmallInteger(maximum=4, default=0)
    is_delete: bool = ormar.Boolean(default=False)

async def create_user():
    """
    初始化一个用户用于测试
    """
    from api.exts.jwt import get_password_hash
    _password = "123456"
    password = get_password_hash(_password)
    await User.objects.create(
        username="test2",
        password=password,
        email="user@user.com",
        mobile="15812341234",
    )

async def with_connect(function):
    async with database:
        await function()

if __name__ == '__main__':
    engine = sqlalchemy.create_engine(DATABASE_URL)
    # just to be sure we clear the db before
    # metadata.drop_all(engine)
    # metadata.create_all(engine)
    asyncio.run(with_connect(create_user))