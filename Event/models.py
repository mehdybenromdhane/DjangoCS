from django.db import models

from django.core.validators import FileExtensionValidator
# Create your models here.
from Person.models import Person

from datetime import datetime
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
    participants = models.ManyToManyField(Person, through="Participation" , related_name="participant")
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        constraints=[
            models.CheckConstraint(check=models.Q(
                evt_date__gt =datetime.now()
            ), name="Please check event date")
        ]
        
        
    

class Participation(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    
    participation_date= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.participation_date}"
    
    class Meta:
        unique_together=['person','event']