from django.db import models

class Product(models.Model):
    prod_id = models.IntegerField(primary_key=True)
#    prod_id = models.IntegerField(unique = True)
    name = models.CharField(max_length=75)
    description = models.TextField()

    def __str__(self):
        return '(' + str(self.prod_id) + ')' + self.name + ' - ' + self.description

    class Meta:
        verbose_name_plural = "Product"

class Order(models.Model):
    order_id = models.CharField(max_length=12)
    name = models.ForeignKey(Product)
    qty = models.IntegerField()

    def __str__(self):
        return '(' + str(self.order_id) + ')' + str(self.name) + ' - ' + str(self.qty)

#Model that stores the coordinates so I can map them
class Load(models.Model):
    time_stamp = models.DateTimeField()
    load_number = models.CharField(max_length=20)
    container_num = models.CharField(max_length=12)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.container_num) + ' (' + str(self.load_number) + '): ' + str(self.latitude) + ', ' + str(self.longitude)
