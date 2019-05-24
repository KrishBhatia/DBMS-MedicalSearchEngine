from django.contrib import admin
from .models import Store, Symptom, Medicine, Disease


class CustomStore(admin.ModelAdmin):
    model = Store
    list_display = ['name', 'city']
    search_fields = ['name']


class CustomMedicine(admin.ModelAdmin):
    model = Medicine
    search_fields = ['name']
    list_display = ['name', 'type']


class CustomDisease(admin.ModelAdmin):
    model = Disease
    search_fields = ['name']


class CustomSymptom(admin.ModelAdmin):
    model = Symptom
    search_fields = ['name']


admin.site.register(Store, CustomStore)
admin.site.register(Symptom, CustomSymptom)
admin.site.register(Medicine, CustomMedicine)
admin.site.register(Disease, CustomDisease)
admin.site.site_header = "Medicare Admin"
admin.site.index_title = "Medicare Administration"
admin.site.site_title = "Medicare Admin"

