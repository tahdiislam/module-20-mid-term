from django.urls import path
from . import views

urlpatterns = [
    # path('create/<int:id>', views.BuyCarView.as_view(), name='create_order')
    path('create/<int:id>', views.buyCar, name='create_order')
]
