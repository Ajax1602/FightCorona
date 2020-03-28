from django.contrib import admin

# Register your models here.
from .models import Service
from .models import SubService
from .models import Request
from .models import State
from .models import District
from .models import Area


class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = Service


class SubServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = SubService


class RequestAdmin(admin.ModelAdmin):
    class Meta:
        model = Request


class StateAdmin(admin.ModelAdmin):
    class Meta:
        model = State


class DistrictAdmin(admin.ModelAdmin):
    class Meta:
        model = District


class AreaAdmin(admin.ModelAdmin):
    class Meta:
        model = Area


admin.site.register(Service, ServiceAdmin)
admin.site.register(SubService, SubServiceAdmin)
admin.site.register(Request, RequestAdmin)

admin.site.register(State, StateAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(District, DistrictAdmin)

