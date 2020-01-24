from django.contrib import admin
from .forms import CustomHospitalCreationForm
from django.utils.html import format_html
from django.urls import path
from django.conf.urls import include, url
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.translation import ugettext_lazy
from user.admin import admin_site
from hospital.models import Hospital

class HospitalAdmin(admin.ModelAdmin):
    form = CustomHospitalCreationForm
    model = Hospital
    list_display = ('hospital_name','registration_no', 'address','status')
    list_filter = ('status',)
    list_per_page = 5  

    fieldsets = (
        (None, {'fields': ('hospital_name','registration_no', 'address','status')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('hospital_name','registration_no', 'address','status')}
        ),
    )
    search_fields = ('hospital_name',)
    ordering = ('-id',)
        
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
        ]
        return my_urls + urls

    def save_hospital(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()

admin_site.register(Hospital,HospitalAdmin)
