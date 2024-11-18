from django.db import models

from django.core.validators import FileExtensionValidator
# Create your models here.
from Person.models import Person

category_list = (
    ('Musique','Musique'),
    ('Cinema','Cinema'),
    ('Sport','Sport'),
)

class Event(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image=models.ImageField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=["jpg","png"])], null=True)
    
    category = models.CharField(max_length=30 , choices=category_list)
    state = models.BooleanField(default=False)
    
    nbr_participant = models.IntegerField(default=0)
    evt_date= models.DateTimeField()
    created_date= models.DateField(auto_now_add=True)
    updated_date= models.DateField(auto_now=True)
    
    organisateur = models.ForeignKey(Person , on_delete=models.SET_NULL , null=True)
    