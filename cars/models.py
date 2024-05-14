from django.db import models
from brands.models import Brand

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='cars/media/uploads/')

    def __str__(self) -> str:
        return f"{self.title}"

#image, title, description, price