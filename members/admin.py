from django.contrib import admin
from .models import Person, Group, Membership


class MembershipAdmin(admin.ModelAdmin):
    readonly_fields = ["joined_at"]


admin.site.register(Membership, MembershipAdmin)
admin.site.register([Person, Group])
