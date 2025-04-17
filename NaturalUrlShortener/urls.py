from django.urls import path
from django.contrib import admin
from NaturalUrlShortener.views import dynamic_handler
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin', admin.site.urls),
    path('<str:slug>', dynamic_handler, name='dynamic-handler'),                # Handle any basic 1-slug url ending in nothing
                                                                                # AND
    path('<str:slug>/', dynamic_handler, name='dynamic-handler'),               # Handle any basic 1-slug url ending in "/"
]