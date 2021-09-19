from django.db import models

# Create your models here.



from django.db import models

class Laptop(models.Model):
    company=models.CharField(max_length=40)
    modelName=models.CharField(max_length=50)
    ram=models.IntegerField()
    rom=models.FloatField()
    processor=models.CharField(max_length=10)
    price=models.FloatField()
    image=models.FileField(upload_to='document/',blank=True)

    def __str__(self):
        return  self.modelName




