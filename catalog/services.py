from catalog.models import Product
from config import settings
from django.core.cache import cache


def get_product_list():
    # проверяю включен ли кеш
    if settings.CACHE_ENABLED:
        # создаю ключ для кеша
        key = 'product_list'
        # проверяю наличие даных по ключу
        product_list = cache.get(key)
        if product_list is None:
            # обращаемся в БД
            product_list = Product.objects.all()
            # сохраняем в кеш
            cache.set(key, product_list)

        return product_list

    else:
        product_list = Product.objects.all()

    return product_list
