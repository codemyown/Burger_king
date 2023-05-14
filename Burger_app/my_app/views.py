from django.shortcuts import render
from django.http import HttpResponse
from .models.contact import Contact
from .models.menu import Menu

# Create your views here.





def index(request):
    menu = Menu.objects.all()
    data  = {
        'menu':menu
    }
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['number']
        email = request.POST['email']
        opt = request.POST['opt']
        date = request.POST['date']
        
        my_contact = Contact(Name = name,Phone_No = phone,Email = email,Persons = opt,date = date)
        my_contact.save()
    return render(request,"index.html",data)
