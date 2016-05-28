from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',

    # django admin
    url(r'^admin/', include(admin.site.urls)),

)
