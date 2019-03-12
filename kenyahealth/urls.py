from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PatientView,RegisterView,LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
router.register('patient',PatientView,base_name='patients'),
# router.register('register',RegisterView,base_name='register')
#create your url patterns here
urlpatterns =[
   url(r'^$',views.index,name="index"),
   url(r'^login/$',views.LoginView.as_view()),
   url(r'^register/$',views.RegisterView.as_view()),
   url(r'^logout/$',views.LogoutView.as_view()),
   url(r'',include(router.urls))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
