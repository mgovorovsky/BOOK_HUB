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
from orders import views as views
from random_number import views as random_number_views
from django.conf.urls.static import static
from django.conf import settings

app_name = "orders" 

urlpatterns = [ 

    path('cart/', views.cart, name = "order_cart"),
    path('cart/<int:pk>/', views.Cart.as_view(), name = "order_cart_pk"),
    path('cart-delete-good/<int:pk>', views.DeleteGoodInCart.as_view(), name = "good_in_cart_delete"),
    path('order_success/', views.order_success, name = "order_success"),
    path('order_data/', views.OrderCreate.as_view(), name = "order_data"),
    path('order_list/', views.OrderList.as_view(), name = "order_list"),
    path("portal_main/", views.portal_view, name="portal_main"),
    path('portal_order/delete/<int:pk>/', views.OrderDelete.as_view(), name="portal_order_delete"),
    path('portal_order/update/<int:pk>/', views.OrderUpdate.as_view(), name="portal_order_update"),
    # path('order_empty/', views.order_success, name = "order_empty"),

] 

if not settings.IS_PRODUCTION:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
