from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import GroupViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('api/v1/', include(router.urls)),
    path('api/v1/posts/<int:post_id>/comments/',
         CommentViewSet.as_view({
             'get': 'list',
             'post': 'create'
         }),
         name='post-comments-list'),
    path('api/v1/posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }),
         name='post-comment-detail'),
]
