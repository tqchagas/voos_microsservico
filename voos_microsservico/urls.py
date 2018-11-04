from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from voos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aeroportos/', views.AeroportoView.as_view()),
    path('voos/', views.VooCriarListar.as_view()),
    path('voos/<int:pk>/', views.VooDetalheApagar.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
