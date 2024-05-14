from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'