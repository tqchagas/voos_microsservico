from django.contrib import admin
from django.urls import path

from voos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aeroportos/', views.AeroportoListar.as_view()),
    path('voos/', views.VooCriarListar.as_view()),
    path('voos/<int:pk>/', views.VooDetalheApagar.as_view())
]
