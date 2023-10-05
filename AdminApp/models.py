from django.db import models

# Create your models here.
class Products(models.Model):
    PID = models.IntegerField()
    PName = models.CharField(max_length=20)
    PCost = models.DecimalField(max_digits=8, decimal_places=2)
    MfDate = models.DateField(auto_now=True)
    EPDate = models.DateField()

    def __str__(self):
        return self.PName
