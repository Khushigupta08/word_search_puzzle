from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_game, name='create_game'),
    path('search/', views.search_game, name='search_game'),
]