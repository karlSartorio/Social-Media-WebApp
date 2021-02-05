from django.contrib import admin
from . import models

#tabular class - allows the dev to utilies the django admin interface website with
# the ability to edit models same page of the parent model
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

# Register your models here.
admin.site.register(models.Group)
