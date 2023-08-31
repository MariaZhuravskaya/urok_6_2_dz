from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Джинсы', 'description': 'Различные модели джинс'},
            {'name': 'Спортивная одежда', 'description': 'В разделе представлена одежда для любого вида спорта: фитнес, йога, бег и др.'},
            {'name': 'Пиджаки', 'description': 'Пиджак – одна из универсальных и необходимых вещей мужского и женского гардеробов. Различные фасоны пиджаков, классические, смокинги, блейзеры и др. '}
        ]

        category_create = []
        for category_item in category_list:
            category_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_create)