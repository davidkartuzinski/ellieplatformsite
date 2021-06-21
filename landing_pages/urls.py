from django.urls import path
from landing_pages import views

app_name = 'pages'

urlpatterns = [
    path('<slug:slug>/', views.single_page, name="single_page"),
]
