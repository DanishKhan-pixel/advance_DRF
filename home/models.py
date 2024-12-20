from django.db import models

# Create your models here.

class people(models.Model):
    person_name=models.CharField(max_length=100)
    person_age=models.IntegerField()

class Transactions(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    transactions_type=models.CharField(max_length= 100 ,choices =
                                       (("CREDIT","CREDIT"),("DEBIT","DEBIT")))
    
    def save(Self, *args, **kwargs ):
        if Self.transactions_type == "CREDIT":
            Self.amount = Self.amount * -1
        return super().save(*args, **kwargs )