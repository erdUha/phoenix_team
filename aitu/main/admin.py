from django.contrib import admin
from .models import Phones
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PhonesRes(resources.ModelResource):
   class Meta:
      model = Phones
class PhonesAdmin(ImportExportModelAdmin):
   resource_class = PhonesRes

admin.site.register(Phones,PhonesAdmin)
