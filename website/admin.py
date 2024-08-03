from django.contrib import admin
from website.models import Record

class RecordsBackEnd(admin.ModelAdmin):
    list_display = (
        'created_at',
        'first_name',
        'last_name',
        'email',
        'city',
        )

admin.site.register(Record, RecordsBackEnd)