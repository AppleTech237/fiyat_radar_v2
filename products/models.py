from django.db import models
from stores.models import Store
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    store = models.ForeignKey(Store, on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url_on_store = models.URLField(max_length=500, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.price} ({self.store.name})" 

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # On enregistre d'abord le prix
        
        alerts_to_update = Alert.objects.filter(
            product=self.product,
            target_price__gte=self.price,
            is_triggered=False
        )
        
       
        for alert in alerts_to_update:
            alert.is_triggered = True
            alert.last_checked_price = self.price
            alert.save()


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_alerts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='alerts')
    target_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    is_triggered = models.BooleanField(default=False, verbose_name="Tetiklendi mi?")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_checked_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Alert for {self.user.username} on {self.product.name}"