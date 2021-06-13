from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .models import CustomUser, EmailConfirmation, Organization


class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email', 'first_name',  'last_name',)
    list_filter = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'first_name',  'last_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_personorg', 'is_org',)}),
        ('Personal', {'fields': ('about', 'slug',)}),
    )
    formfield_overrides = {
        CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)

class EmailConfirmationAdmin(admin.ModelAdmin):

    list_display = ('user', 'first_name', 'last_name', 'email_confirmed', 'activation_key')

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

admin.site.register(EmailConfirmation, EmailConfirmationAdmin)

class OrganizationProfile(admin.ModelAdmin):

    list_display = ('org_name', 'is_verified', 'contact_number')

admin.site.register(Organization, OrganizationProfile)
