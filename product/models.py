from django.db import models
from user.models import User

class Product(models.Model):
    title =models.CharField(max_length=100)
    price = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    info = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    class ProductType(models.TextChoices):
        REAL_ESTATAE = 'REAL_ESTATE'
        VEHICLES = 'VEHICLES'
        DIGITAL_GOODS = 'DIGITAL_GOODS'
        HOME_KITCHEN = 'HOME_KITCHEN'
        SERVICES = 'SERVICES'
        PERSONAL_ITEM = 'PERSONAL_ITEMS'
        ENTERTAINMENT_LEISURE = 'ENTERTAINMENT_LEISURE'
        COMMUNITY = 'COMMUNITY'
        INDUSTRIAL_EQUIPMENT = 'INDUSTRIAL EQUIPMENT'
        JOBS_EMPLOYMENT = 'JOBS & EMPLOYMENT'

    type = models.CharField(  max_length=30, choices=ProductType.choices, null=False, blank=False)
    











