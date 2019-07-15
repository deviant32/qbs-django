from django.urls import include, path
from rest_framework import routers
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from users.views import UserViewSet
from testkit.views import TestKitViewSet
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
urlpatterns = router.urls

schema_view = get_swagger_view(title="API")


router.register(r'users', UserViewSet, basename='user')
router.register(r'testkits', TestKitViewSet, basename='testkit')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^$", schema_view),
    url(r"^auth/", include("rest_auth.urls")),
    url(r"^auth/registration/", include("rest_auth.registration.urls")),
    url(r"^admin/", admin.site.urls),
    url(r"^api-token-auth/", obtain_jwt_token),
    url(r"^api-token-refresh/", refresh_jwt_token),
]


urlpatterns += router.urls
