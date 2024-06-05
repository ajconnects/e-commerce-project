from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("programmer", views.AddProgrammerProfile.as_view(), name='programmer'),
    path("client/", views.AddClientProfile.as_view(), name='client'),
]