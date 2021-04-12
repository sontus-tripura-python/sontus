from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from mysite_app.models import *
# Create your views here.
def home(request):

    portfolio = Portfolio.objects.all()
 
    context = {'portfolio': portfolio}
    
    if request.method == 'POST':
        name =request.POST['name']
        email =request.POST['email']
        subject =request.POST['subject']
        message =request.POST['message']
        #sentTime =request.POST['sentTime']
        if len(name)<6 or len(email)<6 or len(message)<10:
            messages.error(request, "Fail! Please, fill up the form correctly,You missed something")
        else:
            messages.success(request, " thank you ! Your message has been sent successfully. we will contact with you soon ")
        contact = Contact( name=name, email=email, message=message, subject=subject)
        contact.save()
    return render(request, 'mysite/index.html', context)

