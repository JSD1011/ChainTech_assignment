from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('form_page',views.form_page,name='form_page'),
    path('view-submissions/', views.view_submissions, name='view_submissions'),
]
