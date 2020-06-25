from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Queries


@admin.register(Queries)
class QueryAdmin(admin.ModelAdmin):
    list_display = ("query_email", "subject", "message",)
    search_fields = ("query_email", "subject", "message",)


class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        'email', 'username', 'first_name', 'can_access_dashboard', 'last_name', 'work_id', 'phone_number', 'rank',
        'location',)
    list_filter = ('email', 'username', 'location')

    fieldsets = ((None,
                  {'fields': (
                      'email', 'username', 'first_name', 'last_name', 'can_access_dashboard', 'work_id', 'phone_number',
                      'rank',
                      'location',
                      'password',)}),
                 ('Permissions',
                  {'fields': ('is_staff', 'is_superuser', 'is_active')}),
                 )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'username', 'first_name', 'last_name', 'can_access_dashboard', 'work_id', 'phone_number',
                'rank',
                'location',
                'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')}
         ),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name', 'location',)
    ordering = ('email', 'location')


admin.site.register(User, UserAdmin)

admin.site.site_header = "Amanie"
