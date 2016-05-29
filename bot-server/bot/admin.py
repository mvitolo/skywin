from django.contrib import admin
from .models import UserProfile, Team, Player, Match


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'first_name',
                    'last_name',
                    )
    list_display_links = ('username', )
    save_on_top = True
    list_per_page = 20


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
