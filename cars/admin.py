from django.contrib import admin
from .models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug']

admin.site.register(Car, CarAdmin)