"""
URL configuration for backend project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs/', include_docs_urls(title='', public=False)),
    path('admin/', admin.site.urls),
    path('v1/account/', include(('account.urls', 'account'), namespace='accounts-api')),
    path('v1/clothing/', include(('brand.urls', 'brand'), namespace='brand-api')),
    path('v1/electronic/', include(('electronic.urls', 'electronic'), namespace='electronic-api')),
    path('v1/order/', include(('order.urls', 'order'), namespace='order-api')),
    path('v1/restaurant/', include(('restaurant.urls', 'restaurant'), namespace='restaurant-api')),
    path('v1/shipment/', include(('shipment.urls', 'shipment'), namespace='shipment-api')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
