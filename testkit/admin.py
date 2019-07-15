from django.contrib import admin
from users.models import User
from testkit.models import TestKit


@admin.register(TestKit)
class TestKitAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'invoice', )
