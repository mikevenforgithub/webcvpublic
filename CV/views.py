from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .models import *
from django.http import FileResponse


def index(request):
    

    javascript = Pictures.objects.filter(name="javascript").first()
    python = Pictures.objects.filter(name="python").first()
    aws = Pictures.objects.filter(name="aws").first()
    css = Pictures.objects.filter(name="css").first()
    django = Pictures.objects.filter(name="django").first()
    mysql = Pictures.objects.filter(name="mysql").first()

    my_cv = MyCV.objects.filter(title='mycv').first()

    return render(request, "CV/index.html", {
        "javascript": javascript,
        "python": python,
        "aws": aws,
        "django": django,
        "css": css,
        "mysql":mysql,
        "mycv": my_cv
    })

def download(request, id):
    obj = MyCV.objects.get(id=id)
    filename = obj.mycv.path
    response = FileResponse(open(filename, 'rb'))
    return response


