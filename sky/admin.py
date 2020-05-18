from django.contrib import admin

from .models import Stuff, Package, Person, PersonPackage


class PackageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stuff)
admin.site.register(Package, PackageAdmin)
admin.site.register(Person)
admin.site.register(PersonPackage)
