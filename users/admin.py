from django.contrib import admin

from users.models import User
from baskets.admin import BasketAdmin

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdmin,)
