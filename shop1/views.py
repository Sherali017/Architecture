from django.shortcuts import render
from django.views.generic import ListView, DetailView

from shop1.models import ProductModel, CategoryModel


class ProductListView(ListView):
    template_name = 'shop.html'

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category_id=cat)

        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        return context



class ProductDetailView(DetailView):
    template_name = 'shop-single.html'
    model = ProductModel
