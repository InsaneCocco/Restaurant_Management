from django.db import models

class Waiter(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length= 50)


