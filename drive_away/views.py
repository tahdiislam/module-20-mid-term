from typing import Any
from django.views.generic import TemplateView
from brands.models import Brand
from cars.models import Car

class HomePage(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        brand_slug = self.kwargs.get('brand_slug', None)
        if brand_slug is not None:
            brand = Brand.objects.get(slug=brand_slug)
            cars = Car.objects.filter(brand=brand)
        else:
            cars = Car.objects.all()
        brands = Brand.objects.all()
        print('🤣 all brands', brands)
        print('😒 all cars', cars)
        context['brands'] = brands
        context['cars'] = cars
        return context