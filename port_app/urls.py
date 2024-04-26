from django.urls import path
from . import views

urlpatterns = [

    path('', views.portfolio_showcase, name='index_page'),



]