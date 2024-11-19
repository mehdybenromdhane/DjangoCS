from django.contrib import admin

# Register your models here
from .models import Event,Participation


# admin.site.register(Event)


class nbr_ParticipantFilter(admin.SimpleListFilter):
    
    title="number of participant"
    parameter_name="nbr"
    
    def lookups(self, request,model_admin):
        
        return (
            ('No' , ("No participant")),
            ('Yes',("there are participants")),
        )
        
    def queryset(self,request,queryset):
        if self.value()=="No":
            return queryset.filter(nbr_participant__exact=0)
        if self.value()=="Yes":
            return queryset.filter(nbr_participant__gt=0)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display =('title','nbr_participant','description','state','evt_date','category','organisateur')
    list_per_page=1
    list_filter=['category',nbr_ParticipantFilter]
    search_fields=['title','category']
    
    autocomplete_fields=['organisateur']
    
admin.site.register(Participation)