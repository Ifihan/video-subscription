from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movies
from .filters import MoviesFilter
from .forms import CustomUserCreationForm

# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'vsapp/landing.html'


class MovieListView(ListView,LoginRequiredMixin):
    model = Movies
    template_name = 'vsapp/movies_list.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MoviesFilter(self.request.GET, queryset=self.get_queryset())
        return context     


class MovieDetailView(DetailView,LoginRequiredMixin):
    model = Movies
    template_name= 'vsapp/movies_detail.html'


class SignUpView(CreateView):
    template_name = 'vsapp/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')
