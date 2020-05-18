from django.contrib import admin

from .models import Stuff, Package, Person, PersonPackage

admin.site.register(Stuff)
admin.site.register(Package)
admin.site.register(Person)
admin.site.register(PersonPackage)
