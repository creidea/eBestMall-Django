from django.contrib import admin
from goods.models import Goods
from goods.models import GoodsCategory
from goods.models import GoodsCategoryBrand

# Register your models here.
admin.site.register(Goods)
admin.site.register(GoodsCategory)
admin.site.register(GoodsCategoryBrand)
