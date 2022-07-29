from django.contrib import admin
from .models import Develop, QnA
from .models import Brief
# Register your models here.
admin.site.register(Develop)
admin.site.register(QnA)
admin.site.register(Brief)