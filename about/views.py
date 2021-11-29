from django.shortcuts import render
from django.views.generic import ListView

from about.models import AboutModel, FeaturesModel, ClientModel, ProcessModel, VideoModel


class AboutTemplateView(ListView):
    template_name = 'about.html'
    model = AboutModel

    def get_context_data(self, **kwargs):
        context = super(AboutTemplateView, self).get_context_data(**kwargs)
        context['info'] = AboutModel.objects.all()
        context['features'] = FeaturesModel.objects.all()[:3]
        context['clients'] = ClientModel.objects.all()
        context['processes'] = ProcessModel.objects.all()
        context['videos'] = VideoModel.objects.all()

        return context
