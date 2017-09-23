from django.core.urlresolvers import reverse
from django.db import models
from .validations import *
class ContactInfo(models.Model):
    mobile_number= models.CharField(max_length=15,validators=[validate_mobile_number])
    phone_number= models.CharField(max_length=15,validators=[validate_phone_number])
    email_id= models.EmailField()
class Media(models.Model):
    media_id=models.AutoField(primary_key=True)
    media_name= models.CharField(max_length=20)
    media_path= models.FileField(upload_to='documents/')
class PropertyType(models.Model):
    propert_type_id= models.AutoField(primary_key=True)
    description= models.CharField(max_length=50)

    def __str__(self):
        return self.description

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name= models.CharField(max_length=20)
    city_name = models.CharField(max_length=10)
    state_name = models.CharField(max_length=15)

    def __str__(self):
        return self.location_name+ ' - ' + self.city_name+ ' - ' + self.state_name
class Agent(ContactInfo,Media):
    agent_id= models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=20,validators=[validate_first_name])
    last_name= models.CharField(max_length=20,validators=[validate_last_name])
    age=models.IntegerField()
    education= models.CharField(max_length=50,validators=[validate_education])
    company_name=models.CharField(max_length=50)
    specialization= models.CharField(max_length=100,validators=[validate_specialization])
    experience = models.IntegerField()
    agent_notes=models.TextField()
    property_type= models.ManyToManyField("PropertyType")
    location = models.ManyToManyField("Location")
def get_absolute_url(self):
        return reverse('agent-update', kwargs={'pk': self.pk})



class Address(models.Model):
    agent= models.ForeignKey(Agent)
    address_id= models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20,validators=[validate_city])
    state= models.CharField(max_length=20,validators=[validate_state])
    landmark= models.CharField(max_length=20,validators=[validate_landmark])
    pincode= models.IntegerField()

class AgentReferal(models.Model):
    agent= models.ForeignKey(Agent)
    referal_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30,validators=[validate_name])
    verified= models.BooleanField(default=True)


