"""TutionMedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path , include
import jobs.views
import profil.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name= 'home' ),
    path('account/', include('account.urls')),
    path('<int:Tutor_id>/', profil.views.profil, name ='profil' ),
    path('create', jobs.views.create, name = 'create'),
    path('search', jobs.views.search, name = 'search'),
    # url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
