from django.contrib import admin
from .models import Develop
from .models import Brief
from .models import QnA

# Register your models here.
admin.site.register(Brief)
admin.site.register(Develop)
admin.site.register(QnA)