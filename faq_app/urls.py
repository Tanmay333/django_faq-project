from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faq_app.views import FAQViewSet, home_view

router = DefaultRouter()
router.register(r"faqs", FAQViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("api/", include(router.urls)),
]
