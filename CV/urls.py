from django.urls import path
from . import views

urlpatterns = [

   path("mvcv", views.index, name="index"),
   path("mvcv/<int:id>", views.download, name="download"),

]
