"""ong_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from geral.views import home, view_excel
from usuarios.views import register, profile

from django.contrib.auth import urls

admin.site.site_header = 'Administração'
# admin.site.site_title = 'Administração'
# admin.site.index_title = 'Administração'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('', home, name='home'),
    path('financeiro/', include('despesa.urls')),
    path('excel', view_excel, name='excel'),
    url(r'^chaining/', include('smart_selects.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
