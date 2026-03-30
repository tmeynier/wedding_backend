from django.contrib import admin
from .models import Guest

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Guest model.

    This class defines how the Guest model is displayed and interacted with
    within the Django Admin interface.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """
    # Adding 'transport' to the table columns
    list_display = ('first_name', 'last_name', 'transport', 'created_at')
