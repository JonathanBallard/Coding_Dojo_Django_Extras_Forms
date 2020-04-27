


''' 
=============================================================================================== 
=============================================================================================== 
                                   APP-LEVEL URLS.PY: forms_app 
=============================================================================================== 
=============================================================================================== 
''' 



from django.urls import path 
from django.conf.urls import url 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('registerCat/', views.registerCat), 
    path('registerDog/', views.registerDog), 
    path('registerAnimal/', views.registerAnimal), 

] 
