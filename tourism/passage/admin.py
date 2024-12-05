from django.contrib import admin
from .models import User, Coordinates, Levels, Passages, Images

class PassagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'coordinates', 'user', 'status')
    list_filter = ('title', 'user', 'add_time')


admin.site.register(Passages, PassagesAdmin)
admin.site.register(User)
admin.site.register(Coordinates)
admin.site.register(Levels)
admin.site.register(Images)
