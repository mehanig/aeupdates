from django.conf import settings
from django.conf.urls import url, include, patterns
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
from apps.subscriptions import views
from apps.products.views import ProductViewSet
from apps.news.views import NewsViewSet
from apps.stats.views import StatsViewSet
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from aeupdates.views import MainPageView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, 'users')
router.register(r'groups', views.GroupViewSet)
router.register(r'products', ProductViewSet)
router.register(r'news', NewsViewSet, 'news')
router.register(r'stats', StatsViewSet, 'stats')
router.register(r'subscribe', views.SubscribeToNewsBeta, 'subscribe')

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

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    (r'^password/', include('password_reset.urls')),
    url(r'^(?:index.html)?$', MainPageView.as_view()),
    url(r'^manage/(?P<path>.*)$', MainPageView.as_view()),
    url(r'^login/(?P<path>.*)$', MainPageView.as_view()),
    url(r'^signup/(?P<path>.*)$', MainPageView.as_view()),
    url(r'^users/(?P<path>.*)$', MainPageView.as_view()),
    url(r'^token/$', views.ObtainJSONWebTokenPlainJSON.as_view()),
    url(r'^token-refresh/', views.RefreshJSONWebTokenPlainJSON.as_view()),
    url(r'^status/(?P<name>.*)/(?P<version>.*)$', ProductViewSet.as_view({'get': 'retrieve'})),
    # url(r'^token/$', obtain_auth_token)
    # url(r'^rest-auth/', include('rest_auth.urls'))
    url(r'^(?P<path>(?:js|css|img)/.*)$', serve),
)
