from django.conf.urls import patterns, include, url
from django.contrib import admin
from bot.urls import router
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = patterns(
    '',

    # django admin
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^bot/', include('bot.urls')),
    # url(r'^telegrambot/', include('telegrambot.urls', namespace="telegrambot")),
    # url(r'^register/', CreateView.as_view(
    #         template_name='registration/register.html',
    #         form_class=UserCreationForm,
    #         success_url='/bot'), name='register'),

    # Django REST Framework
    # Wire up our API using automatic URL routing. Additionally, we include login URLs for the browsable API.
    url(r'^api/', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)

urlpatterns += (
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^telegrambot/', include('telegrambot.urls', namespace="telegrambot")),
    url(r'^register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/polls'), name='register'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
)
