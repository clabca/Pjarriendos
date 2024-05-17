from django.contrib import admin

# Registrar.
from .models import Propiedad, Region, Comuna

admin.site.register(Propiedad, admin.ModelAdmin)
admin.site.register(Region, admin.ModelAdmin)
admin.site.register(Comuna, admin.ModelAdmin)




