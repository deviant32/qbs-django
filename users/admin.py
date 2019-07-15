from django.contrib import admin
from users.models import User
from testkit.models import TestKit
from allauth.account.models import EmailAddress
from django.contrib.auth.models import Group


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_type', )
    filter_horizontal = ('testkits',)


# Disable allauth model
admin.site.unregister(EmailAddress)

# Disable groups
admin.site.unregister(Group)
