
from django.urls import path
from . import views

urlpatterns = [
    path('publicaciones/', views.publicaciones_view, name='publicaciones')
]