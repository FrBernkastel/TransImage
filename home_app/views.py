from django.shortcuts import render
from TransImage.settings import BASE_DIR
from home_app.models import IMG
from PIL import Image
from cyclegan import rec
import os

# Create your views here.
def home_page(request):
    context={
    "IMG0":"/media/default.jpg",
    "IMG1":"/media/default2.jpg",
    }
    return render(request,'main.html',context)

def upload_img(request):

    if request.method=='POST':
        fileObj=request.FILES.get("img_file")
        sav_fn = os.path.join(BASE_DIR,"media/original.jpg")
        with open(sav_fn,'wb+') as sav:
            for chunk in fileObj.chunks():
                sav.write(chunk)
    image_o = Image.open(sav_fn)
    image_new = image_o.convert("RGB")
    image_new.save(sav_fn)

    return render(request,'main.html')


def generate_img(request):
    options = [request.POST.get('v1'),request.POST.get('v2'),request.POST.get('v3'),request.POST.get('v4')]
    print (options)
    rec.transfer(options)

    return render(request,'main.html')