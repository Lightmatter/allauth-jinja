from allauth.account.utils import user_display as allauth_user_display
from django_jinja import library

@library.global_function
def user_display(user):
    """
    Example usage::

        {{ user_display(request.user) }}
    """
    return allauth_user_display(user)