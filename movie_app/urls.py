from django.urls import path
from .views import (
    DirectorListCreateView, DirectorDetailView,
    MovieListCreateView, MovieDetailView,
    ReviewListCreateView, ReviewDetailView
)

urlpatterns = [
    # Режиссеры
    path('v1/directors/', DirectorListCreateView.as_view(), name='director-list'),
    path('v1/directors/<int:id>/', DirectorDetailView.as_view(), name='director-detail'),

    # Фильмы
    path('v1/movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('v1/movies/<int:id>/', MovieDetailView.as_view(), name='movie-detail'),

    # Отзывы
    path('v1/reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('v1/reviews/<int:id>/', ReviewDetailView.as_view(), name='review-detail'),
]
