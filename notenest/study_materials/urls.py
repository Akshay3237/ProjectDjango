from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('material', views.material_view, name='material'),
    path('create_material/', views.create_material, name='create_material'),
    
]
