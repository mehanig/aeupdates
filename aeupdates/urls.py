from django.conf import settings
from django.conf.urls import url, include, patterns
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from apps.subscriptions import views
from apps.products.views import ProductViewSet
from django.contrib import admin
from django.contrib.staticfiles.views import serve


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, 'users')
router.register(r'groups', views.GroupViewSet)
router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# Add urls to resetting passwords
include('password_reset.urls')

if settings.DEBUG:
    urlpatterns += [
      url(r'^static/(?P<path>.*)$', serve),
    ]

# TODO: (MY) /aeupdates/aeupdates/urls.py:26: RemovedInDjango110Warning: Support for string view arguments to url()
# is deprecated and will be removed in Django 1.10 (got serve). Pass the callable instead.
# url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'ember/index.html'}),

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    (r'^password/', include('password_reset.urls')),
    url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'ember/index.html'}),
    url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
    url(r'^manage/(?P<path>.*)$', 'serve', kwargs={'path': 'ember/index.html'}),
    url(r'^login/(?P<path>.*)$', 'serve', kwargs={'path': 'ember/index.html'}),
    url(r'^signup/(?P<path>.*)$', 'serve', kwargs={'path': 'ember/index.html'}),
    url(r'^token/$', obtain_auth_token)
    # url(r'^rest-auth/', include('rest_auth.urls'))
)
