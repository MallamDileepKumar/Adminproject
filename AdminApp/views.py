from django.shortcuts import render
from .models import Products
from django.views import View
# Create your views here.
class PDview(View):
    def get(self,request):
        Roshan = Products.objects.all()
        return render(request,'display.html',{'Roshan': Roshan})

