from django.db import models


class TextileWaste(models.Model):
    MATERIAL_CHOICES = [
        ('Cotton', 'Cotton'),
        ('Polyester', 'Polyester'),
        ('Silk', 'Silk'),
        ('Wool', 'Wool'),
        ('Denim', 'Denim'),
    ]

    material_type = models.CharField(max_length=100, choices=MATERIAL_CHOICES)
    quantity = models.FloatField()
    color = models.CharField(max_length=50)
    source = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.material_type} - {self.quantity} kg"
