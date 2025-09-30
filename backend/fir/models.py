from django.db import models
from users.models import CustomUser

class FIR(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Investigating', 'Investigating'),
        ('Closed', 'Closed'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.status})"
