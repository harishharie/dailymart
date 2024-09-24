from django.shortcuts import render,redirect
from.models import*
from adminapp.models import*
from django.db.models.aggregates import Sum


# Create your views here.
def userapp(request):
    c=request.session.get('u_id')
    data3=cart.objects.filter(cartuser=c,status=0).count()
    data=catagories.objects.all()
    data2=products.objects.all()
    return render(request,'userapp.html',{'data':data,'data2':data2,'data3':data3})   
def about(request):
    return render(request,'about.html')
def categorycard(request):
   data=catagories.objects.all()  
   return render(request,'categorycard.html',{'data':data})

def productcard(request,category):
   if(category == "all"):
    data=products.objects.all()
   else:
       data=products.objects.filter(category=category)
   return render(request,'productcard.html',{'data':data})

def viewmore(request,id):
    data=products.objects.filter(id=id)
    return render(request,'viewmore.html',{'data':data})
def contact(request):
        return render(request,'contact.html')

def contactdata(request):
    if request.method=="POST":
     name=request.POST["name"]
     email=request.POST["email"]
     message=request.POST["message"]
     data=contact1(name=name,email=email,message=message)
     data.save()
     return redirect("contact")
def login(request):
        return render(request,'login.html')

def register(request):
    return render(request,'register.html')
def registerdata(request):
    if request.method=="POST":
     username=request.POST["username"]
     password=request.POST["password"]
     email=request.POST["email"]
     phonenumber=request.POST["phonenumber"]
     data=Register(username=username,email=email,password=password,phonenumber=phonenumber)
     data.save()
     return redirect("login")
def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Register.objects.filter(username=username,password=password).exists():
           data = Register.objects.filter(username=username,password=password).values('id','phonenumber','email').first()
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['phonenumber'] 
           request.session['email_u'] = data['email'] 
           request.session['username_u'] = username
           request.session['password_u'] = password
           return redirect('login') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('login')

def userlogout(request):
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('login')

def Cart(request):   
    c=request.session.get('u_id')
    a=cart.objects.filter(cartuser=c,status=0).aggregate(Sum('total'))
    data=cart.objects.filter(cartuser=c,status=0)
    return render(request,"cart.html",{'data':data,'a':a})

def cartdata(request,id):
    if request.method=="POST":
        user_id=request.session.get('u_id')
        quantity=request.POST['quantity']
        total=request.POST['total']
        data=cart(cartuser=Register.objects.get(id=user_id),cartproduct=products.objects.get(id=id),quantity=quantity,total=total)
        data.save()
        return redirect('Cart')
def cartdelete(request,id):
     cart.objects.filter(id=id).delete()
     return redirect('Cart') 

def Checkout(request):   
    c=request.session.get('u_id')
    b=cart.objects.filter(cartuser=c,status=0).aggregate(Sum('total'))
    data=cart.objects.filter(cartuser=c,status=0)
    return render(request,"checkout.html",{'data':data,'b':b})

def checkoutdata(request):
    if request.method=="POST":
        checkoutid=request.session.get('u_id')
        address=request.POST['address']
        city=request.POST['City']
        country=request.POST['country']
        postcode=request.POST['postcode']

        buy=cart.objects.filter(cartuser=checkoutid,status=0)

        for i in buy:
         data=checkout(usercheckout=Register.objects.get(id=checkoutid),checkoutcart=cart.objects.get(id=i.id),address=address,city=city,country=country,postcode=postcode)
         data.save()
         cart.objects.filter(id=i.id).update(status=1)
        return redirect('success') 
def success(request):
    s=request.session.get('u_id')
    data=checkout.objects.filter(usercheckout=s)
    return render(request,'success.html',{'data':data})

def sample(request):
    pass


# vvvvvvv