from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('cryptography/', include('cryptography.urls')),
    path('instructions/', views.instructions),
    path('contact/', views.contact),
]
urlpatterns += staticfiles_urlpatterns()
