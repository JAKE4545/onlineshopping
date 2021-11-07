# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 22:03
# @Author  : JAKE4545
# @Email   : tmwu2018@163.com
import ormar
import sqlalchemy
import asyncio

from . import BaseMeta, DATABASE_URL,database,metadata


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=20, unique=True)
    email: str = ormar.String(max_length=30, unique=True)
    password: str = ormar.String(max_length=255)
    mobile: str = ormar.String(max_length=12, unique=True)
    user_level: int = ormar.SmallInteger(maximum=4)
    is_delete: bool = ormar.Boolean(default=False)


async def create_user():
    await User.objects.create(
        username="admin",
        hashed_password="123456",
        is_admin=True,
    )

async def with_connect(function):
    # note that for any other backend than sqlite you actually need to
    # connect to the database to perform db operations
    async with database:
        await function()

if __name__ == '__main__':
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    asyncio.run(with_connect(create_user))