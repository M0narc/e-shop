from django.db import models

from base.models import CustomUser
from products.models import Product
from django.core.validators import MinValueValidator


class Order(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    tax_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {self._id} by {self.user}"


class OrderItem(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, 
                              blank=True, 
                              default=0, 
                              validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=7, 
                                decimal_places=2, 
                                null=True, blank=True, 
                                validators=[MinValueValidator(0)])
    # image = models.ImageField(null=True, blank=True) # tengo que modificarlo para que apunte al lugar correcto

    class Meta:
        ordering = ['order', 'product']
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.qty} x {self.product.name if self.product else 'Unknown'}"

    def get_image_url(self):
        return self.product.image.url if self.product else None
