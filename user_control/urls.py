from django.urls import path, include
from user_control import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter(trailing_slash = True)

router.register("create-user",views.CreateUserView, "create user")
router.register("login",views.LoginView, "login")
router.register("update-password",views.UpdatePasswordView, "update password")
router.register("me",views.MeView, "me")
router.register("activities-log",views.UserActivitiesView, "activities log")
router.register("users", views.UsersView, "users")

urlpatterns = [
    path("",include(router.urls))
]
