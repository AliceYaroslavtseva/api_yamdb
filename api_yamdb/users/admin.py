from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import User


class UserResourse(resources.ModelResource):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'role', 'bio', 'first_name', 'last_name'
        )
        list_display = (
            'id', 'username', 'email', 'role', 'bio', 'first_name', 'last_name'
        )
        export_order = (
            'id', 'username', 'email', 'role', 'bio', 'first_name', 'last_name'
        )


class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResourse


admin.site.register(User, UserAdmin)
