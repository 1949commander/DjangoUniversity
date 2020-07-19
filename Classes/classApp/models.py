from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    Course_Num = models.IntegerField(default="", blank=True, null=False)
    Instruct_Name = models.TextField(max_length=60, default="", blank=True)
    Duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

