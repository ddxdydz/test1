from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import GroupViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('api/v1/groups', GroupViewSet)
router.register('api/v1/posts', PostViewSet)
router.register(r'api/v1/posts/\d/comments', CommentViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
