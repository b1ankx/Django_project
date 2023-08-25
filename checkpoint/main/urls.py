from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('About', views.About, name='About'),
    path('create', views.create, name='create')
]
