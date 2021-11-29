from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CommentModelForm
from blog.models import AuthorModel, PostModel


class Blogview(ListView):
    template_name = 'blog.html'


    def get_queryset(self):
        qs = PostModel.objects.all
        # q = self.request.GET.get('q')
        # cat = self.request.GET.get('cat')
        #
        # if q:
        #     qs.filter(title__icontains=q)
        #
        # if cat:
        #     qs = qs.filter(category_id=cat)

        return qs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['categories'] = CategoryModel.objects.order_by('-pk')
    #     return context


class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = PostModel

class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk':self.kwargs.get('pk')})
