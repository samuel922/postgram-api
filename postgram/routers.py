from rest_framework_nested import routers

from postgram.comment.viewsets import CommentViewSet
from postgram.user.viewsets import UserViewSet
from postgram.auth.viewsets.register import RegisterViewSet
from postgram.auth.viewsets.login import LoginViewSet
from postgram.auth.viewsets.refresh import RefreshViewSet

from postgram.post.viewsets import PostViewSet

router = routers.SimpleRouter()

############################ AUTH ROUTES  ##################
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

######################## USER ROUTES  #######################
router.register(r'user', UserViewSet, basename='user')

#######################  POST ROUTES #########################
router.register(r'post', PostViewSet, basename='post')

####################### COMMENT ROUTES #######################
posts_router = routers.NestedSimpleRouter(router, r'post', lookup='post')
posts_router.register(r'comment', CommentViewSet, basename='post-comment')

urlpatterns = [
    *router.urls,
    *posts_router.urls
]
