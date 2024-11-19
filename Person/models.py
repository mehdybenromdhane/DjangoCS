from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.core.exceptions import ValidationError
def validate_cin(value):
    if len(value)!=8:
        raise ValidationError("cin must has 8 characters")
        
        

def validate_email(value):
    if str(value).endswith('@esprit.tn') == False:
        raise ValidationError("email must ends with @esprit.tn")

    
    
class Person(AbstractUser):
    cin = models.CharField(primary_key=True,max_length=8 , validators=[validate_cin])
    email= models.EmailField(max_length=100 , validators=[validate_email])
    username=models.CharField(max_length=20,unique=True)
    
    USERNAME_FIELD='username'
    
   
    
    class Meta:
        verbose_name="Person"
    
    