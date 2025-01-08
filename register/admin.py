from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Extend UserAdmin to display full name and phone number
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    list_display = ('username', 'email', 'get_phone_number', 'get_full_name', 'is_staff')
    
    def get_phone_number(self, obj):
        return obj.profile.phone_number
    get_phone_number.short_description = 'Phone Number'
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.short_description = 'Full Name'

# Unregister the default User model and register the customized one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register Profile for separate visibility in admin (optional)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
