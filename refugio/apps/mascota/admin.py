# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from apps.mascota.models import Vacuna, Mascota 

admin.site.register(Vacuna)
admin.site.register(Mascota)
