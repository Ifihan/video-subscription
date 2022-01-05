from django.urls import path
import vsapp
from vsapp import views
from .views import MovieListView,MovieDetailView,ReviewCreate,review_list,review_detail
from django.conf import settings
from django.conf.urls.static import static


app_name = 'vsapp'

urlpatterns = [
    path('',MovieListView.as_view(),name='movies_list'),
    path('movie/<slug>',MovieDetailView.as_view(),name ='movies_detail'),
    #path('movie/<slug>/(<movie_id>[0-9]+,)/add_review/', views.add_review, name='add_review'),
    path(route="movie/<slug:slug>/review",view=ReviewCreate.as_view(),name="review",),
    path('review_list/', views.review_list, name='review_list'),
    path('review/(<review_id>[0-9]+)/', views.review_detail, name='review_detail'),
]

if settings.DEBUG is True:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
