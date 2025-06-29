from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('WMS/', include('WMS.urls')),        #여기가 추가된것
    path('', views.index, name='index'),  # '/' 에 해당되는 path
]