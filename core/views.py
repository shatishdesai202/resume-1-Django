from django.shortcuts import render
from .models import Contact
# Create your views here.

def index(request):
    context = {'home':'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        company = request.POST.get('company')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        form = Contact(name=name, email=email, company=company, phone=mobile, message=message)
        form.save()

    context = {'contact':'active'}
    return render(request, 'core/contact.html', context)