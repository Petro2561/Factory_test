from django.contrib import admin
from visits.models import Store, Visit, Worker


class WorkerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number")
    search_fields = ("name",)


class StoreAdmin(admin.ModelAdmin):
    list_display = ("title", "worker")
    search_fields = ("title",)


class VisitsAdmin(admin.ModelAdmin):
    list_display = ("store", "latitude", "longitude", "visit_date", "get_worker")
    search_fields = ("store__title", "store__worker__name")

    def get_worker(self, obj):
        return obj.store.worker.name


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Visit, VisitsAdmin)
