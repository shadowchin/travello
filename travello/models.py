from django.db import models

# Create your models here.

class destination(models.Model):

    # no ID required because mySQL uses uniques IDs. 'id : int'
    # search for Django model field to look at what field can be used
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.FloatField()
    offer = models.BooleanField(default = False)