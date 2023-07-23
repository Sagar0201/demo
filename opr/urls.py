from django.urls import path
from . import views

urlpatterns = [
     path("all-data/",views.all_data,name="all_data"),
     path("single-data/",views.single_data,name="single_data"),
     path("filter-data/",views.filter_data,name="filter_data"),
     path("add-data/",views.add_data,name="add_data"),
     path('get-add-data/',views.get_add_data,name="get_and_add_data"),
]

