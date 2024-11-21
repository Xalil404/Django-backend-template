from django.contrib import admin
from .models import Profile

# Optionally, you can create a custom admin interface for Profile if needed
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'image')  # Customize fields as needed
    search_fields = ('user__username',)  # Add search functionality by user name


# Register the Profile model with the custom admin interface
admin.site.register(Profile, ProfileAdmin)
