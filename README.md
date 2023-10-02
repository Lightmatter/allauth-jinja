# allauth-jinja
[![Version](https://img.shields.io/pypi/v/allauth-jinja?style=for-the-badge&logo=pypi&logoColor=fff)](https://pypi.org/project/allauth-jinja/)
[![Python](https://img.shields.io/pypi/pyversions/allauth-jinja?style=for-the-badge&logo=python&logoColor=fff)](https://pypi.org/project/allauth-jinja/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&logo=pypi&logoColor=fff)](https://www.gnu.org/licenses/gpl-3.0)

The complete set of [django-allauth](https://github.com/pennersr/django-allauth) templates rewritten in jinja.

## Installing
```pip install allauth-jinja```

## Quick Start
Add allauth_jinja to your installed apps above allauth, e.g.
```
INSTALLED_APPS = [
  ...
  allauth_jinja,
  allauth,
  ...
]
```

In your templates settings for jinja you must have at least the following
```
{
  "APP_DIRS": True,
  "OPTIONS": {
    "match_extension": None,
    "app_dirname": "jinja2",
    "undefined": "jinja2.Undefined",
    "context_processors": [
      "django.template.context_processors.request",
      "django.contrib.messages.context_processors.messages",
      ...
    ],
    "globals": {
      ...,
      "user_display": "allauth_jinja.account.templatetags.account.user_display",
      ...
    }
  }
}
```

Depending on what templates you use you'll need to add the relevant global functions.
