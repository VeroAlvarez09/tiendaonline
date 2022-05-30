from django.db import models
from pets.models import Product

class DocumentType(models.Model):
    name = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=20, default="")
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Shopping(models.Model):
    name_lastname = models.CharField(max_length=200, default="")
    id_document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    id_city = models.ForeignKey(City, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    document = models.CharField(max_length=50)
    email = models.EmailField()
    direction = models.CharField(max_length=255)
    cellphone = models.IntegerField()
    total = models.FloatField()
    date = models.DateTimeField("date create")
