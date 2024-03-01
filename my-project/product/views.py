from django.shortcuts import render, reverse
from .models import product
from django.http import HttpResponseRedirect
from category.models import Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django import forms
from category.models import Category
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


# Create your views here.


def getProducts(request):
    context = {'data':product.objects.all()}
    return render(request , 'product/product.html' , context )


#================= genirc =====================

# @login_required()
# class AddProductView(View):
#     template_name = 'product/insert.html'

#     @method_decorator(login_required)
#     def get(self, request):
#         categories = Category.objects.all()
#         form = ProductForm()
#         return render(request, self.template_name, {'form': form, 'categories': categories})

#     @method_decorator(login_required)
#     def post(self, request):
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.category_id = request.POST.get('category')
#             product.save()
#             return redirect('product')
#         else:
#             categories = Category.objects.all()
#             return render(request, self.template_name, {'form': form, 'categories': categories})
 
        
@login_required()
def addProducts(request):
    if (request.method == 'POST'):
        name = request.POST['name']
        price = request.POST['price']
        details = request.POST['details']
        image = request.FILES['image']
        category_id = request.POST['category']
        
        try:

          category = Category.objects.get(id=category_id)
          product.objects.create(name=name , price = price , details=details,image=image,category=category)
          return HttpResponseRedirect(reverse('product'))
        except:
          pass
    categories = Category.objects.all()
    return render(request,'product/insert.html',{'categories': categories})
#==================================================================================

def delProducts(request,id):
    product.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('product'))
#===============================================================================
@login_required()
def updateProducts(request, id):
    context = {}
    Product = product.objects.get(id=id)
    
    if request.method == 'POST':
        Product.name = request.POST['name']
        Product.price = request.POST['price']
        Product.details = request.POST['details']

        if 'image' in request.FILES:
            Product.image = request.FILES['image']
        category_id = request.POST['category']
        try:
            category_instance = Category.objects.get(id=category_id)
            Product.category = category_instance
        except Category.DoesNotExist:
            pass
        
        Product.save()
        return HttpResponseRedirect(reverse('product'))
    context['Product'] = Product
    context['categories'] = Category.objects.all()
    return render(request, 'product/update.html', context)

#==========generic update==========

# @login_required()
# class UpdateProductView(UpdateView):
#     model = product
#     form_class = ProductForm
#     template_name = 'product/update.html'
#     success_url = reverse_lazy('product')

#=======================================================================
data = [
        {"id" : 1 , "name" : "Iphone" },
        {"id" : 2 , "name" : "Samsong" },
        
        
    ]
@login_required()
def category(request):
    context= {'data' : data}
    return render(request,"product/category.html" , context)
#=================================================================================

def registration(request):
    if request.method == 'POST':
      form= UserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data['username']
          password = form.cleaned_data['password1']
          user = authenticate(username=username , password=password)
          login(request, user)
          messages.success(request, ('Registration Done ! You are now logged in'))
          return  redirect("home")
    else:
         form= UserCreationForm()

    return render(request,'registration/registration.html',{'form':form})