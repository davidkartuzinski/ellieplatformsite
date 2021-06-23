from django.urls import path
from . import views

app_name = 'landing_page'

urlpatterns = [
    path('<slug:slug>/', views.single_page, name='single_page'),
]
