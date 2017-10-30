from django.contrib import admin

# Register your models here.
from .models import RawBillingRecord,ValidatedBillingRecord,BadBillingRecord

admin.site.register(RawBillingRecord)
admin.site.register(ValidatedBillingRecord)
admin.site.register(BadBillingRecord)
