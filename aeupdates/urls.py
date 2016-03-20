from django.conf import settings
from django.conf.urls import url, include, patterns
from rest_framework import routers
from apps.subscriptions import views
from django.contrib.staticfiles.views import serve
from .views import MainPageView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += [
      url(r'^static/(?P<path>.*)$', serve),
    ]

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'ember/index.html'}),
    url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
    url(r'^users/(?P<path>.*)$', MainPageView.as_view()),
    url(r'^login/(?P<path>.*)$', MainPageView.as_view()),
    url(r'^manage/(?P<path>.*)$', MainPageView.as_view()),
)
