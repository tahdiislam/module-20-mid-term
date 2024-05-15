from django.urls import path
from . import views

urlpatterns = [
    path('details/<slug:slug>', views.CarDetailsView.as_view(), name='car_details')
]
