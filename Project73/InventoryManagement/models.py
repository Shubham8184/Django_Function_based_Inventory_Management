from django.db import models



class Product(models.Model):
    date=models.DateField()
    provider=models.CharField(max_length=30)
    productname=models.CharField(max_length=30)
    price=models.FloatField()
    qty=models.IntegerField()
    amount=models.FloatField()
    stock=models.IntegerField()


    def __str__(self):
        return self.provider


