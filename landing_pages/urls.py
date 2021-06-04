from django.conf.urls import url
from landing_pages import views

urlpatterns = [
    url(r'^$', views.index, name='lp_index'),
]
