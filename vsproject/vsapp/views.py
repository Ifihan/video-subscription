from django.shortcuts import render

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'vsapp/landing.html'