from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from sketchbookapi.views import register_user, login_user
from rest_framework import routers
from sketchbookapi.views import PostView
from sketchbookapi.views import MediumView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', PostView, 'post')
router.register(r'mediums', MediumView, 'medium')
urlpatterns = [
    
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
       
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
