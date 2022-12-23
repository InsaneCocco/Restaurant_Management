from django.db import models

class Order_list(models.Model):
    table = models.IntegerField()
    total = models.IntegerField()


