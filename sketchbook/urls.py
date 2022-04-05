from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from sketchbookapi.views import register_user, login_user
from rest_framework import routers
from sketchbookapi.views import PostView
from sketchbookapi.views import MediumView
from sketchbookapi.views import MoodView
from sketchbookapi.views import CommentView
from sketchbookapi.views import ArtistView
from sketchbookapi.views import MediumPostView
from sketchbookapi.views import ChecklistView
from django.conf.urls.static import static, settings

router = routers.DefaultRouter(trailing_slash=False)
# The trailing_slash=False tells the router to accept /gametypes instead of /gametypes/. It’s a very annoying error to come across, when your 
# server is not responding and the code looks right, the only issue is your fetch url is missing a / at the end.
router.register(r'posts', PostView, 'post')
router.register(r'mediums', MediumView, 'medium')
router.register(r'moods', MoodView, 'mood')
router.register(r'comments', CommentView, 'comment')
router.register(r'artists', ArtistView, 'artist')
router.register(r'mediumposts', MediumPostView, 'mediumpost')
router.register(r'checklists', ChecklistView, 'checklist')
urlpatterns = [
    
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
       
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
