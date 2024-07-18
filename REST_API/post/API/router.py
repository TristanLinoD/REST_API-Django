from rest_framework.routers import DefaultRouter
from .views import PostApiView

router_posts = DefaultRouter()
router_posts.register(prefix='post', basename='post', viewset=PostApiView)