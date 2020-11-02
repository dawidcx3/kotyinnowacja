from django.contrib import admin
from .models import Color
from .models import Cat
from .models import Prey
from .models import Hunting
from .models import Usr

# Register your models here.

class CatAdmin(admin.ModelAdmin):
    readonly_fields = ('gender',)
    
admin.site.register(Cat, CatAdmin)
admin.site.register(Color)
admin.site.register(Prey)
admin.site.register(Hunting)
admin.site.register(Usr)