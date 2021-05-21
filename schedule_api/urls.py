from django.urls import path, include
from rest_framework import routers
from schedule import views


router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r"todo", views.TodoViewSet)
router.register(r"comment", views.CommentViewSet)

urlpatterns = [
    path("schedule/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
