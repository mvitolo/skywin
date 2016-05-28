from django.conf.urls import patterns


urlpatterns = patterns(
    'bot.views',

    # Home
    (r'^[/]?$', 'home', {'template_name': 'bot/home.html'}, 'bot_home'),

)
