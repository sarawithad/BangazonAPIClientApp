from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        ordering = ('created',)

    
class ProductType(models.Model):
    """
    Purpose: Expose Product Type data to Client
    Author: Dara Thomas
    """
    category = models.CharField(max_length = 30)

class PaymentType(models.Model):
    """
    Purpose: Expose Payment Type data to Client
    Author: Harry Epstein
    """
    account_number = models.IntegerField()
    customer = models.ForeignKey(Customer)

class Order(models.Model):
    '''
    Purpose: Expose Order data to Client
    Author: Miriam Rozenbaum
    '''
    created = models.DateField(blank=True, null=True)
    customer = models.ForeignKey(Customer)
    payment_type = models.ForeignKey(PaymentType)


class Product(models.Model):
    '''
    Purpose: Expose Product data to Client
    Author: Bri Wyatt
    '''
    price = models.FloatField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created = models.DateField()
    product_type = models.ForeignKey(ProductType)
    customer = models.ForeignKey(Customer)


class OrderProduct(models.Model):
    order = models.ForeignKey(
      Order,
      on_delete=models.DO_NOTHING,
      related_name='line_items',
    )
    product = models.ForeignKey(
      Product,
      on_delete=models.DO_NOTHING,
      related_name='line_items',
    )
