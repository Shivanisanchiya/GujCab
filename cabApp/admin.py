from django.contrib import admin
from .models import Oneway,RoundTrip,Packages,Cabs
from import_export.admin import ExportActionMixin
# Register your models here.

# admin.site.register(Oneway)
def getFieldsModel(model):
    return [field.name for field in model._meta.get_fields()]

@admin.register(Oneway)
class OnewayAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = getFieldsModel(Oneway)
    list_filter = ("date","CabChoice")
    search_fields = ('name','CabChoice','Mo_No','FromCity')
    list_max_show_all = (10)

    def has_add_permission(self, request):
        return False

@admin.register(RoundTrip)
class RoundTripAdmin(admin.ModelAdmin):

    list_display = getFieldsModel(RoundTrip)
    list_filter = ("dateOfJourney","cabChoice")
    search_fields = ('name','mo_No','fromCity','cabChoice')
    list_max_show_all = (10)

    def has_add_permission(self, request):
        return False

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = getFieldsModel(Packages)
    list_filter = ("PackageName",)
    search_fields = ("PackageName",)
    list_max_show_all = (10)

admin.site.register(Cabs)

