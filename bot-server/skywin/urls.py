from django.conf.urls import patterns, include, url
from django.contrib import admin
from bot.urls import router


urlpatterns = patterns(
    '',

    # django admin
    url(r'^admin/', include(admin.site.urls)),

    # Django REST Framework
    # Wire up our API using automatic URL routing. Additionally, we include login URLs for the browsable API.
    url(r'^api/', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)
