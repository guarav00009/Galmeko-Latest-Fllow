
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from .models import User
from hospital.models import Hospital
from django.urls import path
from django.conf.urls import include, url
from django.template.response import TemplateResponse
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ugettext_lazy
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect

class MyAdminSite(admin.AdminSite):
    index_title = ugettext_lazy('Admin')

    def each_context(self, request):
        """
        Return a dictionary of variables to put in the template context for
        *every* page in the admin site.

        For sites running on a subpath, use the SCRIPT_NAME value if site_url
        hasn't been customized.
        """
        self.site_title = ugettext_lazy('User')
        self.index_title = ugettext_lazy('Dashboard')
        self.site_header = ugettext_lazy('GLEMKO')

        script_name = request.META['SCRIPT_NAME']
        site_url = script_name if self.site_url == '/' and script_name else self.site_url
        return {
            'site_title': self.site_title,
            'site_header': self.site_header,
            'site_url': site_url,
            'has_permission': self.has_permission(request),
            'available_apps': self.get_app_list(request),
            'is_popup': False,
        }

    def get_urls(self):
        urls = super(MyAdminSite, self).get_urls()
        my_urls = [     
        ]
        return my_urls + urls


admin_site = MyAdminSite()

class HospitalInline(admin.TabularInline):
    model = Hospital

class UserAdmin(UserAdmin):
    inlines = [
        HospitalInline
    ]
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('first_name','last_name', 'email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    list_per_page = 10  # No of records per page
    fieldsets = (
        (None, {'fields': ('first_name','last_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active','type')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin_site.register(User, UserAdmin)
