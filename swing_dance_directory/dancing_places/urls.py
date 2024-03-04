from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('about/', views.about_view, name='about'),
    path('add-spot/', views.add_spot, name='add_spot'),
    path('submission-success/', views.submission_success, name='submission_success'),
]
