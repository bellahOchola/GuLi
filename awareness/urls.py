from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, include

urlpatterns = [
   path('',  views.index, name='index'),
   path('about/', views.about, name='about'),
   path('work/', views.work, name='work'),
   path('contact/', views.contact, name='contact')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)