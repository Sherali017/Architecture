from django.shortcuts import render
from django.views.generic import ListView, DetailView

from projects.models import projectModel, CategoryModel


class ProjectView(ListView):
    template_name = 'projects.html'
    queryset = projectModel

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['projects'] = projectModel.objects.all()

        return context

class ProjectDetailView(DetailView):
    template_name = 'project-detail.html'
    model = projectModel

