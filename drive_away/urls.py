from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('user/', include('users.urls')),
    path('cars-filter-by-brand/<slug:brand_slug>', views.HomePage.as_view(), name='filter_home'),
    path('car/', include('cars.urls')),
    path('order/', include('orders.urls'))
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)