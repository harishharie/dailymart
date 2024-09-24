from django.urls import path
from.import views

urlpatterns = [
    path('userapp',views.userapp,name='userapp'),
    path('about',views.about,name='about'),
    path('categorycard',views.categorycard,name='categorycard'),
    path('productcard/<str:category>',views.productcard,name='productcard'),
    path('viewmore/<int:id>',views.viewmore,name='viewmore'),
    path('contact',views.contact,name='contact'),
    path('contactdata',views.contactdata,name='contactdata'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('registerdata',views.registerdata,name='registerdata'),
    path('publicdata',views.publicdata,name='publicdata'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('Cart',views.Cart,name='Cart'),
    path('cartdata/<int:id>',views.cartdata,name='cartdata'),
    path('cartdelete/<int:id>',views.cartdelete,name='cartdelete'),

    path('Checkout',views.Checkout,name='Checkout'),
    path('checkoutdata',views.checkoutdata,name='checkoutdata'),
    path('success',views.success,name='success'),











]
