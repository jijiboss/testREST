from django.db import models

class Product(models.Model):
    prod_id = models.IntegerField(primary_key=True)
#    prod_id = models.IntegerField(unique = True)
    name = models.CharField(max_length=75)
    description = models.TextField()

    def __str__(self):
        return '(' + str(self.prod_id) + ')' + self.name + ' - ' + self.description

class Order(models.Model):
    order_id = models.CharField(max_length=12)
    name = models.ForeignKey(Product)
    qty = models.IntegerField()

    def __str__(self):
        return '(' + str(self.order_id) + ')' + str(self.name) + ' - ' + str(self.qty)
