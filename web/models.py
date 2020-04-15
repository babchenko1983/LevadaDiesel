from django.db import models
from django.urls import reverse


class Product(models.Model):
    FORCE = 'force'
    POMPE = 'pompe'
    CHOICE_GROUP = (
        (FORCE, 'force'),
        (POMPE, 'pompe'),
    )

    name = models.CharField(max_length=30, db_index=True)
    number = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    group = models.CharField(max_length=20, choices=CHOICE_GROUP, default=FORCE)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    stock = models.PositiveIntegerField()
    image = models.ImageField(default='pictures/product_image/noimage.png', upload_to='pictures/product_image')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('number', 'slug')

    def get_absolute_url(self):
        return reverse("single", kwargs={
            'slug': self.slug
        })
