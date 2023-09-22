from django.contrib import admin

from catalog.models import Category, Product, Contact, Blog, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'categoria')
    list_filter = 'categoria',
    search_fields = ('name', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('header', 'content', 'image', 'date_creation', 'number_views', 'is_publication', 'slug')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'name_version', 'flag')
    list_filter = 'flag',
    search_fields = ('product', 'name_version')

