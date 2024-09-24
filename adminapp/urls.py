from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('form',views.form,name='form'),
    path('categorydata',views.categorydata,name='categorydata'),
    path('table',views.table,name='table'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),

    path('form2',views.form2,name='form2'),
    path('productdata',views.productdata,name='productdata'),
    path('table2',views.table2,name='table2'),
    path('edit2/<int:id>',views.edit2,name='edit2'),
    path('update2/<int:id>',views.update2,name='update2'),
    path('delete2/<int:id>',views.delete2,name='delete2'),
    path('table3',views.table3,name='table3'),
    path('table4',views.table4,name='table4'),
    path('userdata',views.userdata,name='userdata'),



]
