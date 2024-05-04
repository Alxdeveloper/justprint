from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('TS','Tshirt'),
    ('DR','Diaries'),
    ('UM','Umbrellas'),
    ('RL','Reflectors'),
    ('Cp','Caps'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField()
    composition = models.TextField(default='') 
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    image = models.ImageField(upload_to='product')
    
    def __str__(self) -> str:
        return self.title