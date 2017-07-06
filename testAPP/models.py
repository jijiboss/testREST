from django.db import models

class Product(models.Model):
    prod_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    description = models.TextField()

    def __str__(self):
        return '(' + self.prod_id + ')' + self.name + ' - ' + self.description
