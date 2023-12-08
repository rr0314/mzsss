from django.urls import path
from mzapp import views

urlpatterns = [
    path('',views.home),
 
    path('cform/', views.cform),
    path('eform/', views.eform),
    path('emform/', views.emform),
    path('contact/', views.contact),
    path('about/', views.about),
    path('faq/', views.faq),
    path('gallery/', views.gallery),
    path('incform/', views.incform),
    path('mal/', views.mal),
    path('members/', views.members),
    path('service/', views.service),
    path('success/', views.success)
]
