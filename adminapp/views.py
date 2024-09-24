from django.shortcuts import render,redirect
from.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from userapp.models import*


# Create your views here.
def home(request):
    category=catagories.objects.all().count()
    product=products.objects.all().count()
    register=Register.objects.all().count()
    contact=contact1.objects.all().count()
    Checkout=checkout.objects.all().count()


    return render(request,'adminapp.html',{'category':category,'product':product,'register':register,'contact':contact,'Checkout':Checkout})
def form(request):
    return render(request,"form.html")
def categorydata(request):
    if request.method=="POST":
     name=request.POST["name"]
     image=request.FILES["image"]
     data=catagories(name=name,image=image)
     data.save()
     return redirect("home")
def table(request):
   data=catagories.objects.all()
   return render(request,'table.html',{'data':data})
def edit(request,id):
   data=catagories.objects.filter(id=id)
   return render(request,'edit.html',{'data':data})
def update(request,id):
   if request.method=="POST":
     name=request.POST["name"]
     try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
     except MultiValueDictKeyError:
            file = catagories.objects.get(id=id).image
     catagories.objects.filter(id=id).update(name=name,image=file)
     return redirect('table')
def delete(request,id):
     catagories.objects.filter(id=id).delete()
     return redirect('table')
def form2(request):
    data=catagories.objects.all()
    return render(request,'form2.html',{'data':data})
def productdata(request):
    if request.method=="POST":
     name=request.POST["name"]
     image=request.FILES["image"]
     price=request.POST["price"]
     category=request.POST["category"]
     features=request.POST["features"]         
     data=products(name=name,image=image,price=price,category=category,features=features)
     data.save()
     return redirect("home")
def table2(request):
   data=products.objects.all()
   return render(request,'table2.html',{'data':data})
def edit2(request,id):
   data=products.objects.filter(id=id)
   data2=catagories.objects.all()
   
   return render(request,'edit2.html',{'data':data,'data2':data2})
def update2(request,id):
   if request.method=="POST":
     name=request.POST["name"]
     price=request.POST["price"]
     category=request.POST["category"]
     features=request.POST["features"]   
     try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
     except MultiValueDictKeyError:
            file =products.objects.get(id=id).image
     products.objects.filter(id=id).update(name=name,image=file,price=price,category=category,features=features)
     return redirect('table2')
def delete2(request,id):
     products.objects.filter(id=id).delete()
     return redirect('table2')  
def table3(request):
   data=Register.objects.all()
   return render(request,'table3.html',{'data':data}) 
def table4(request):
   data=contact1.objects.all()
   return render(request,'table4.html',{'data':data}) 
def userdata(request):
    data=checkout.objects.all()
    return render(request,'userdetails.html',{'data':data}) 
    

