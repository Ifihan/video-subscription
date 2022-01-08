"""vsproject URL Configuration

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
from django.contrib import admin
from django.urls import path,include
import vsapp.urls
from vsapp.views import LandingPageView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
admin.site.site_header = 'Vsapp Administration'
admin.site.site_title = 'Movies Administration'
admin.site.index_title = 'Movies Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vsapp/',include('vsapp.urls',namespace='vsapp')),
    path('',LandingPageView.as_view(),name='landing-page'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

