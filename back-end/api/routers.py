from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.healthy.views import ApiHealthyViewSet
from api.auth.views import AuthAPIView

router = DefaultRouter()

router.register("healthy", viewset=ApiHealthyViewSet, basename="healthy")
router.register("register", viewset=AuthAPIView, basename="register")

urlpatterns = [path("", include(router.urls))]
