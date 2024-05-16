from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from .models import Order
from cars.models import Car
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
# class BuyCarView(RedirectView):
#     def post(self, request, id):
#         car = Car.objects.get(pk=id)
#         Order.objects.create(buyer=request.user, car=car)
#         return reverse_lazy('profile')
#     def get(self, request, id):
#         return reverse_lazy('profile')

@login_required
def buyCar(request, id):
    if request.method == 'POST':
        car = Car.objects.get(pk=id)
        Order.objects.create(buyer=request.user, car=car)
        Car.objects.filter(pk=id).update(quantity=car.quantity - 1)
        messages.success(request, f"{car.title} buy successfully")
        return redirect('profile')
    else:
        return redirect('home')