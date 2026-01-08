from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    website_url = models.URLField()
    image = models.ImageField(upload_to='stores/', null=True, blank=True)

    def __str__(self):
        return self.name