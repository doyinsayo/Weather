from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)
    postcode = models.IntegerField()

    def __str__(self):
        #This is to allow the name of the city be shown in the database as it is typed
        #and not as a Cityobject
        return self.name   

    class Meta:
        #This is to pluralize the Model(City) in the database
        verbose_name_plural = 'Cities'    
        