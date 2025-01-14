
from django.db import models
from baykeshop.public.abstract import AbstractModel, ContentTypeAbstract


class BaykeIPAddress(AbstractModel):
    """ 统计站点来访IP """
    ip = models.GenericIPAddressField(null=True, blank=True)
    browser = models.TextField(max_length=500, blank=True, default="")
    address = models.CharField(max_length=150, blank=True, default="")

    class Meta:
        verbose_name = 'BaykeStatsIPAddress'
        verbose_name_plural = 'BaykeStatsIPAddress'

    def __str__(self):
        return self.address


class BaykeStats(ContentTypeAbstract):
    """ pv 和 uv统计 """
    pv = models.BigIntegerField(default=0)
    uv = models.BigIntegerField(default=0)

    class Meta:
        verbose_name = 'BaykeStats'
        verbose_name_plural = 'BaykeStatss'

    def __str__(self):
        return f"pv:{self.pv} | uv: {self.uv}"


