from django.contrib import admin
from .models.contact import Contact
from .models.menu import Menu
# Register your models here.




class ContactAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Persons']
    
    
class MenuAdmin(admin.ModelAdmin):
    list_display  = ['Menu_Name',"price"]
    
    
admin.site.register(Contact,ContactAdmin)
admin.site.register(Menu,MenuAdmin)
    
    
