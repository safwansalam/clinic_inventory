from django.db import models

class Medicine(models.Model):

    CATEGORY_CHOICES = [
        ('Tablet','Tablet'),
        ('Syrup','Syrup'),
        ('Injection','Injection'),
        ('Capsule','Capsule'),
    ]

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    manufacturer = models.CharField(max_length=200)
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
