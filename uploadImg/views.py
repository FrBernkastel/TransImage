from django.shortcuts import render

# Create your views here.
from uploadImg.models import IMG

def uploadImg(request):
    if request.method=='POST':
        print (str(request.FILES.get('img')))
        new_img = IMG(img=request.FILES.get('img'))
        new_img.save()
    return render(request, 'uploadimg.html')


def showImg(request):
    imgs = IMG.objects.all()
    content={
    'imgs':imgs
    }
    return render(request, 'showimg.html',content)



