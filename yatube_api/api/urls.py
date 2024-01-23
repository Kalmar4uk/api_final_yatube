from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(r'api/v1/posts', PostViewSet)
router_v1.register(r'api/v1/groups', GroupViewSet)
router_v1.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('api/v1/', include('djoser.urls.jwt')),
    path(
        'api/v1/follow/',
        FollowViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='following'
    )
]
