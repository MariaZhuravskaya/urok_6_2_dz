from django.urls import path
from catalog.views import index, ContactListView, ProductListView, CategoryListView, ProductDetailView, BlogCreateView, \
    BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionCreateView, VersionListView, VersionUpdateView, VersionDeleteView, VersionDetailView

urlpatterns = [
    path('', index),
    path('contacts', ContactListView.as_view(), name='contact_list'),
    path('products', ProductListView.as_view(), name='product_list'),
    path('catalog_products', CategoryListView.as_view(), name='category_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/create', ProductCreateView.as_view(), name='product_form'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),

    path('version', VersionListView.as_view(), name='version_list'),
    path('version/create', VersionCreateView.as_view(), name='version_form'),

    path('version/detail/<int:pk>', VersionDetailView.as_view(), name='version_detail'),
    path('version/update/<int:pk>', VersionUpdateView.as_view(), name='version_update'),
    path('version/delete/<int:pk>', VersionDeleteView.as_view(), name='version_delete'),


    path('blog/create', BlogCreateView.as_view(), name='blog_form'),
    path('blog/detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog', BlogListView.as_view(), name='blog_list'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]
