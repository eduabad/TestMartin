from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from superheroes import views

urlpatterns = [
    url('heroes', views.HeroeList.as_view()),
    url('heroes', views.HeroeDetail.as_view()),
    url('publisher', views.PublisherList.as_view()),
    url('publisher', views.PublisherList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)