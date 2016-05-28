

def create_user_profile(backend, user, response, *args, **kwargs):
    # Create a new UserProfile instance if the User is signing in for the first time
    from .models import UserProfile

    try:
        UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=user,
                                   has_accepted_terms_and_conditions=True,
                                   is_email_verified=True,  # emails from social signup are 'double opt-in'
                                   )
        user_profile.save()
