from django.contrib import admin
from .models import ticketform, contactform

# Admin customization for ticketform model
class ticketformAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'quantity', 'dropdown_option', 'uploaded_file')  # Fields to display in the admin panel

# Registering ticketform with the customized admin
admin.site.register(ticketform, ticketformAdmin)


# Admin customization for contactform model
class contactformAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # Fields to display in the admin panel

# Registering contactform with the customized admin
admin.site.register(contactform, contactformAdmin)

from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'event_date', 'event_time', 'price', 'date_created')
    list_filter = ('category', 'event_date')
    search_fields = ('title', 'category', 'description')