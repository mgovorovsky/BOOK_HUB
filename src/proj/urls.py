"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, reverse_lazy
from directories import views as directories_views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('applications/', include("applications.urls")),
    path('directories/', include("directories.urls")),
    path('main/', directories_views.book_types),
    path('orders/', include("orders.urls")),
    path('random_number/', include("random_number.urls")),


] 

if not settings.IS_PRODUCTION:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
