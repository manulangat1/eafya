from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views
from django.conf import settings
from django.conf.urls.static import static
#create your url patterns here
urlpatterns =[
   url(r'^$',views.index,name="index")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
