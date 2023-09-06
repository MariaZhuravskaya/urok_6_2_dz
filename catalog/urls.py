from django.urls import path
from catalog.views import index, ContactListView, ProductListView, CategoryListView, ProductDetailView, BlogCreateView, \
    BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', index),
    path('contacts', ContactListView.as_view(), name='contact_list'),
    path('products', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('catalog_products', CategoryListView.as_view(), name='category_list'),

    path('blog/create', BlogCreateView.as_view(), name='blog_form'),
    path('blog/detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog', BlogListView.as_view(), name='blog_list'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]
