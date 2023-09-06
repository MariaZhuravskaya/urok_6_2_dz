from django.db import models

NULLABLE = {'blank': True, 'null': True}


#  Добавьте модель «Порода» с полями: название, описание.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='изображение')
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')
    date_change = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=16, verbose_name='Телефон', **NULLABLE)
    message = models.TextField(verbose_name='Сообщение', **NULLABLE)

    def __str__(self):
        return f"""{self.name}, {self.phone}, {self.message}"""

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Blog(models.Model):
    header = models.CharField(max_length=50, verbose_name='Имя')
    content = models.TextField(verbose_name='Cодержимое', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='изображение')
    date_creation = models.DateField(auto_now_add=True, verbose_name='дата создания')

    number_views = models.IntegerField(default=0, verbose_name='количество просмотров')
    is_publication = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return f"""{self.header}, {self.slug}, {self.content}"""

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'