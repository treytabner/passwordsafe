from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from passwordsafe import views


router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'credentials', views.CredentialViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'passwordsafe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
