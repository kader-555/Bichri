from django.urls import path
from .views import ListUserByRatingAV, RatingListAV, UserListAV

urlpatterns = [
    path('list/',UserListAV.as_view(),name = 'user-list'),
    path('ratings/',RatingListAV.as_view(),name = 'rating-list'),
    path('ratings/<int:rating>/', ListUserByRatingAV.as_view(), name='list-users-by-rating'),
]