from django.db import models

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self)->str:
        #string conversion
        return self.title



# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    inventory = models.SmallIntegerField()
    #on_delete is used to prevent deletion of a catogory until all the menu items of that category gets deleted frirst
    category = models.ForeignKey(Category, on_delete=models.PROTECT,default = 1)
