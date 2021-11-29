from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import PostModel
from home.models import SpecializationModel, TeamModel, projectsModel, NewsModel, PartnerModel, ClientsModel


class HomeView(ListView):
    template_name = 'index.html'
    model = SpecializationModel
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['special'] = SpecializationModel.objects.all()[:3]
        context['projects'] = projectsModel.objects.all()
        context['staff'] = TeamModel.objects.all()[:3]
        context['news'] = NewsModel.objects.order_by('-pk')[:3]
        context['partners'] = PartnerModel.objects.all()
        context['clients'] = ClientsModel.objects.all()
        return context


    paginate_by = 3

class ServiceDetailView(DetailView):
    template_name = 'service-detail.html'
    model = SpecializationModel


# class NewsDetailView(DetailView):
#     template_name = 'blog-detail.html'
#     model = PostModel



