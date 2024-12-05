

from django.db import models
from django.contrib.auth import get_user_model

from baykeshop.public.abstract import AbstractModel
from baykeshop.models import BaykeShopSKU

User = get_user_model()


class BaykeShopingCart(AbstractModel):
    """ 购物车数据模型 """
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="用户")
    sku = models.ForeignKey(BaykeShopSKU, on_delete=models.PROTECT, verbose_name="商品sku")
    num = models.PositiveIntegerField(default=0, verbose_name="数量")
    
    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(fields=['owner', 'sku'], name='unique_owner_sku')
        ]
        
    def __str__(self):
        return f'{self.owner}{self.sku}'
    
    @classmethod
    def get_cart_count(cls, user):
        # 当前用户的购物车商品数量
        return sum(list(cls.objects.filter(owner=user).values_list('num', flat=True)))