# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 22:03
# @Author  : JAKE4545
# @Email   : tmwu2018@163.com
import ormar
from . import BaseMeta

class SKUImage(ormar.Model):
    class Meta(BaseMeta):
        tablename = "sku_image"

    id: int = ormar.Integer(primary_key=True)
    image: str = ormar.String(max_length=100)

class SKU(ormar.Model):
    class Meta(BaseMeta):
        tablename = "sku"

    id: int = ormar.Integer(primary_key=True)

    name:str = ormar.String(max_length=50)
    caption:str = ormar.String(max_length=100, verbose_name='副标题')
    spu = models.ForeignKey(SPU, related_name='skus', on_delete=models.CASCADE, verbose_name='商品')
    category = models.ForeignKey(GoodsCategory, on_delete=models.PROTECT, verbose_name='从属类别')
    # category_id====>category对象的id
    price: float = ormar.Decimal(max_digits=10, decimal_places=2)
    cost_price: float = ormar.Decimal(max_digits=10, decimal_places=2, verbose_name='进价')
    market_price: float = ormar.Decimal(max_digits=10, decimal_places=2, verbose_name='市场价')
    stock: float = ormar.Integer(default=0, verbose_name='库存')
    sales: float = ormar.Integer(default=0, verbose_name='销量')
    comments: float = ormar.Integer(default=0, verbose_name='评价数')
    is_launched: bool = ormar.Boolean(default=True, verbose_name='是否上架销售')
    default_image: str = ormar.String(max_length=200, default='', null=True, blank=True, verbose_name='默认图片')