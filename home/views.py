from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,HttpResponse,redirect
from .forms import  ImageForm
from .models import Imagemodel
import cv2
def index(request):
    return(render(request,"base.html"))

def modelform(request):
    # if request.method=='POST':
    #     form=ImageForm(request.POST,request.FILES)
    #
    #     if form.is_valid():
    #         form.save()
    #         print(Imagemodel.objects.all())
    #         obj=Imagemodel.objects.all().last()
    #         print(obj.faceimg.url)
    #         # print(obj[0].faceimg.url)
    #         dobackend(request,image=obj.faceimg.url)
    #         # return redirect('result',image=obj.faceimg.url)
    # else:
    #     form=ImageForm()
    # return(render(request,"model.html", {"form": form}))
    if request.method == 'POST' and request.FILES['inpfile']:
        myfile = request.FILES['inpfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(filename)
    else:
        return render(request,"model.html")


def dobackend(request,image):
    # faceimg=cv2.imread("./"+image)
    # cv2.imshow("My Face",faceimg)
    result(request)

def result(request):
    # faceimg=cv2.imread("./"+image)
    # cv2.imshow("your face",faceimg)
    # myfaceimg=cv2.imread("media/testing/"+form.faceimg.url)
    return render(request,"result.html")
    # return HttpResponse(request,"<h1>Your Images is uploaded successfully</h1>")