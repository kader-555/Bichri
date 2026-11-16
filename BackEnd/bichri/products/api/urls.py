from django.urls import path
from .views import CategoryListAV, ProductAV,ProductDetailAV, ProductListByCategoryAV, ProductListByCityAV,CityListAV
urlpatterns = [
    path('list/', ProductAV.as_view(),name ='product-list'),
    path('<int:pk>/', ProductDetailAV.as_view(),name ='product-detail'),
    path('category/<int:category_id>/', ProductListByCategoryAV.as_view(), name='product-list-by-category'),
    path('city/<int:city_id>/', ProductListByCityAV.as_view(), name='product-list-by-city'),
    path('categories/', CategoryListAV.as_view(), name='category-list'),
    path('cities/', CityListAV.as_view(), name='city-list'),
]
