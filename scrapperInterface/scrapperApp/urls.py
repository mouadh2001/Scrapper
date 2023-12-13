from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),

    # Add more paths for other sections of your site
]
