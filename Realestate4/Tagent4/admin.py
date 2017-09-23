from django.contrib import admin

from .models import Location
from .models import Address
from .models import Agent
from .models import PropertyType
admin.site.register(Agent)
admin.site.register(Address)
admin.site.register(Location)
admin.site.register(PropertyType)