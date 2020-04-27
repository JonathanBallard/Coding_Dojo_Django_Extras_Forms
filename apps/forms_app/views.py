from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
from .forms import *
 
 
# Create your views here. 
def index(request): 
    catForm = RegisterCatForm()
    allCats = Cat.objects.all()

    dogForm = RegisterDogForm()
    allDogs = Dog.objects.all()


    animalForm = RegisterAnimalForm()
    allAnimals = Animal.objects.all()




    context = {
        'catForm' : catForm,
        'dogForm' : dogForm,
        'animalForm' : animalForm,
        'all_cats' : allCats,
        'all_dogs' : allDogs,
        'all_animals' : allAnimals,

    }


    return render(request, 'forms_app/index.html', context) 



def registerCat(request):

    newCat = Cat.objects.create(name=request.POST['name'], desc=request.POST['desc'])

    return redirect('/forms/')


def registerDog(request):

    newDog = Dog.objects.create(name=request.POST['name'], desc=request.POST['desc'])

    return redirect('/forms/')



def registerAnimal(request):
    bound_form = RegisterAnimalForm(request.POST)

    print('BOUND FORM =================================================================')
    print(bound_form.is_valid())
    print(bound_form.errors)

    if bound_form.is_valid():
        newAnimal = Animal.objects.create(name=request.POST['name'], desc=request.POST['desc'], color=request.POST['color'], age=request.POST['age'], weight=request.POST['weight'], height=request.POST['height'], animal_type = request.POST['animal_type'])
    else:
        messages.error(request, bound_form.errors)
        print(messages.error)
    return redirect('/forms/')





