from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('api/v1/', include(v1_router.urls)),
    path('api/v1/', include('djoser.urls.jwt')),
    path(
        'api/v1/follow/',
        FollowViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='following'
    )
]
