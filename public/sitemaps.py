

from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.sitemaps import FlatPageSitemap

from baykeshop import models


class BaykeShopSPUSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return models.BaykeShopSPU.objects.filter(is_del=False)

    def lastmod(self, obj):
        return obj.pub_date
    
    
class BaykeShopCategorySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return models.BaykeShopCategory.objects.filter(is_del=False)

    def lastmod(self, obj):
        return obj.pub_date
    

sitemaps = {
    'spu': BaykeShopSPUSitemap,
    'cate': BaykeShopCategorySitemap,
    'flatpage': FlatPageSitemap
}