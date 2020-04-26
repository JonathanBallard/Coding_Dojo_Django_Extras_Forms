from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
from .forms import RegisterForm
 
 
# Create your views here. 
def index(request): 
    form = RegisterForm()
    allCats = Cat.objects.all()
    context = {
        'regForm' : form,
        'all_cats' : allCats,
    }
    return render(request, 'forms_app/index.html', context) 



def register(request):

    newCat = Cat.objects.create(name=request.POST['name'], desc=request.POST['desc'])

    return redirect('/')





