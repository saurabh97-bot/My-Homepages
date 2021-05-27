from django.shortcuts import render
from .models import page,ImageSlider

# Create your views here.

def index(request):

    s = page.objects.all()
    tom = ImageSlider.objects.all()
    context = {
        's': s,
        'tom': tom
    }

    return render(request,'index.html',context=context)


def detail(request,pk):
    s = page.objects.get(pk=pk)
    context = {
        's':s
    }

    return render(request,'detail.html',context=context)


def banner(request):
    tom = ImageSlider.objects.all()

    return render(request, 'slider.html', {'tom': tom})
