from django.shortcuts import render , reverse
from .forms import AddCategory
from .models import Category
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth.decorators import login_required


def getCategory(request):
    context = {'Data':Category.objects.all()}
    return render(request , 'category/Clist.html' , context )


def addCategory(request):
    form=AddCategory()
    context={'form':form}
    
    if(request.method=='POST'):
        form=AddCategory(request.POST)
        if(form.is_valid()):
            name = form.cleaned_data['name']
            if Category.objects.filter(name=name).exists():
                    form.add_error('name', 'Category with this name already exists.')
            else:
             Category.objects.create(name=request.POST['name'])
    return render(request , 'category/category.html',context)      