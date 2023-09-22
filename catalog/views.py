import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Category, Blog, Version


def index(request):
    if request.method == 'GET':
        list_product = Product.objects.all()
        return render(request, 'catalog/index.html', {'products': list_product})


class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.all()


class CategoryListView(ListView):
    model = Category


#########   Продукт


class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(categoria_id=self.request.GET.get('categoria_id'))
        return queryset


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:category_list')


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = Version.objects.filter(product=context['object'], flag=True).first()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get("pk"))
        return queryset


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category_list')


#############   Блог


class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'content', 'image',)
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_publication=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'content', 'image',)

    # success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.header)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')


# ВЕРСИИ

class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm

    success_url = reverse_lazy('catalog:version_list')

    def form_valid(self, form):

        versions_item = Version.objects.all()
        if versions_item == 0:
            return super().form_valid(form)
        else:
            for version in versions_item:
                if int(form.data['product']) == version.product.id:
                    if version.flag:
                        version.flag = False
                        version.save()
                        return super().form_valid(form)


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:version_list')

    def form_valid(self, form):

        versions_item = Version.objects.all()

        for version in versions_item:
            if int(form.data['product']) == version.product.id:
                if version.flag:
                    version.flag = False
                    version.save()
                    return super().form_valid(form)

class VersionListView(ListView):
    model = Version


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:version_list')


class VersionDetailView(DetailView):
    model = Version
    success_url = reverse_lazy('catalog:category_list')

