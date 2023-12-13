from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('create_contact',views.create_contact,name='create_contact'),
    path('update_contact/<con_id>',views.update_contact,name='update_contact'),
    path('contact_details/<con_id>',views.contact_details,name="contact_details"),
    path('delete_contact/<con_id>',views.delete_contact,name='delete_contact')]