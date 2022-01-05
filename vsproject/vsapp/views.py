from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movies,Review
from .filters import MoviesFilter
from .forms import CustomUserCreationForm,ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime

# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'vsapp/landing.html'


class MovieListView(ListView):
    model = Movies
    template_name = 'vsapp/movies_list.html'  
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MoviesFilter(self.request.GET, queryset=self.get_queryset())
        return context     


class MovieDetailView(DetailView,LoginRequiredMixin):
    model = Movies
    context_object_name = 'movies'
    template_name= 'vsapp/movies_detail.html'
    queryset = Movies.objects.all()


class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm    
    context_object_name = 'reviews'
    template_name = 'reviews/review.html'   

    def get_success_url(self):
        return reverse('vsapp:movies_detail', kwargs={'slug':Review.slug})


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


