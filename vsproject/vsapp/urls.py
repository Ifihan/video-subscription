from django.urls import path
#import vsapp
#from vsapp import views
from .views import MovieListView,MovieDetailView,ReviewCreate

app_name = 'vsapp'

urlpatterns = [
    path('',MovieListView.as_view(),name='movies_list'),
    path('movie/<slug>',MovieDetailView.as_view(),name ='movies_detail'),
    path(route="movie/review/<slug:slug>/",view=ReviewCreate.as_view(),name="review",),
]
