from django.urls import path
from .views import  form_del_pinturas, form_mod_pinturas, form_pinturas, home, Pinturas

urlpatterns = [
    path('', home, name= "home"),
    path('pinturas/', Pinturas, name= "Pinturas"),
    path('form-pinturas/', form_pinturas, name= "form_pinturas"),
    path('form-mod-pinturas/<id>', form_mod_pinturas, name= "form_mod_pinturas"),
    path('form-del-pinturas/<id>', form_del_pinturas, name= "form_del_pinturas"),
    path('inicio/', home, name= "home"),

]  