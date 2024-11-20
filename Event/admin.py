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



def refuse_state(ModelAdmin,request,queryset):
    queryset.update(state=False)


def accept_state(ModelAdmin,request,queryset):
    queryset.update(state=True)


class ParticipationInline(admin.TabularInline):
    model= Participation
    extra=5
    readonly_fields=('participation_date',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display =('title','nbr_participant','description','state','evt_date','category','organisateur')
    list_per_page=1
    list_filter=['category',nbr_ParticipantFilter]
    search_fields=['title','category']
    
    actions=[accept_state,refuse_state]
    autocomplete_fields=['organisateur']
    
    inlines=[ParticipationInline]
    
    
    fieldsets = (
    ('A propos', {"fields": ('title','description','image'),}),
    ('Date',{"fields":('evt_date',) }),
    ('Others',{"fields":('category','state','nbr_participant') }),
    ('Personal',{"fields":('organisateur',) })
    )
    
    
    
    
    
admin.site.register(Participation)