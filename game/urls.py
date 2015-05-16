from django.conf.urls import patterns, include, url
from rest_framework import routers
from dishes.api import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'dishes', views.DishViewSet)

urlpatterns = patterns(
    '',

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)
