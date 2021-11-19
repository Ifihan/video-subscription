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


class MovieListView(ListView,LoginRequiredMixin):
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

    """def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        Movies = self.get_movies()
        return context

    def get_movies(self):
        moviess = get_object_or_404(Movies, slug=self.kwargs["slug"])
        return moviess

    def get_queryset(self):
        Movies = self.get_movies()
        return Movies.objects.all()"""


class SignUpView(CreateView):
    template_name = 'vsapp/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')

class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm    
    context_object_name = 'reviews'
    template_name = 'reviews/review.html'   


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

def add_review(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.movie = movie
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('vsapp:movies_detail', args=[movie.id,]))

    return render(request, 'vsapp/movies_detail.html', {'movie': movie, 'form': form})    

