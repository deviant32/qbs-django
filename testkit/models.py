import uuid
from django.db import models
from datetime import datetime
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices
from django.conf import settings
from django.utils.translation import gettext as _


class TestKit(models.Model):
    STATUS = Choices('available', 'processing', 'complete')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=datetime.now)
    status = StatusField(choices=STATUS, default=STATUS.available)

    # this would eventually reference another model possibly with the invoice details
    invoice = models.CharField(
        null=True, blank=True, max_length=10, default="")

    # possibly reference another model, not sure what the result would look like
    results = models.CharField(
        null=True, blank=True, max_length=10, default="")

    class Meta:
        verbose_name = 'Test Kit'
        verbose_name_plural = 'Test Kits'
