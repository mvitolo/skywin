from django import template
from django.conf import settings


register = template.Library()


def domain_url():
    """
    Returns the string contained in the setting DOMAIN_URL.

    insert the following in the template:
    {% load custom_tags %}{% domain_url %}
    """
    return settings.DOMAIN_URL


def privacy_policy_url():
    """
    Returns the string contained in the setting PRIVACY_POLICY_URL.

    insert the following in the template:
    {% load custom_tags %}{% privacy_policy_url %}
    """
    return settings.PRIVACY_POLICY_URL


def fb_app_id():
    """
    Returns the string contained in the setting FACEBOOK_APP_ID.

    insert the following in the template:
    {% load custom_tags %}{% fb_app_id %}
    """
    return settings.FACEBOOK_APP_ID


def email_address_for_support():
    """
    Returns the string contained in the setting EMAIL_ADDRESS_FOR_SUPPORT.

    insert the following in the template:
    {% load custom_tags %}{% email_address_for_support %}
    """
    return settings.EMAIL_ADDRESS_FOR_SUPPORT


def format_date_range(date_from, date_to, separator=" - ", format_str="%d %b %Y", year_f=" %Y", month_f=" %b"):
    """
    Takes a start date, end date, separator and formatting strings and returns a pretty date range string.

    insert the following in the template:
    {% load custom_tags %}{% format_date_range date_from date_to %}
    """
    if date_to and date_from and date_to.strftime(format_str) != date_from.strftime(format_str):
        from_format = to_format = format_str
        if date_from.year == date_to.year:
            from_format = from_format.replace(year_f, '')
            if date_from.month == date_to.month:
                from_format = from_format.replace(month_f, '')
        return separator.join((date_from.strftime(from_format), date_to.strftime(to_format)))
    else:
        return date_from.strftime(format_str)


domain_url = register.simple_tag(domain_url)
privacy_policy_url = register.simple_tag(privacy_policy_url)
fb_app_id = register.simple_tag(fb_app_id)
email_address_for_support = register.simple_tag(email_address_for_support)
format_date_range = register.simple_tag(format_date_range)
