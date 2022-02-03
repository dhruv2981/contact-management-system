from django.contrib import admin

from family.models import FamilyHead, FamilyMembers

# Register your models here.
admin.site.register(FamilyHead)
admin.site.register(FamilyMembers)
