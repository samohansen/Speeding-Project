from django.db import models
from datetime import datetime, timedelta


class Driver(models.Model) :
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    homeTown = models.CharField(max_length=50, blank=True)

    def __str__(self) :
        return (self.full_name)
    
    @property
    def full_name(self) :
        return '%s %s' % (self.fName, self.lName)

    def save(self) :
        self.fName = self.fName.upper()
        super(Driver, self).save()

class Ticket(models.Model) :
    date = models.DateField(default=datetime.today)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    locationStreet = models.CharField(max_length=50, blank=True)
    locationCity = models.CharField(max_length=50)
    speedMPH = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    # This should be a One to Many field, but I'm not sure how to show that yet
    driver = models.OneToOneField(Driver, models.CASCADE) 


