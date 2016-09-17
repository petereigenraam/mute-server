from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class State(models.Model):
    """
    Docstrings are only dragging us down.
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('user'))
    state = models.BooleanField(verbose_name=_('state'), default=(False))
