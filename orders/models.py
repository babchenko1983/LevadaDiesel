from django.db import models
from web.models import Product

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Finished", "Finished"),)


class Order(models.Model):
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Started")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    postal_code = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    delivery=models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    number = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return '{}'.format(self.id)




