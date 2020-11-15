from django.contrib import admin
from .models import Guide, Jumbotron


class JumbotronAdmin(admin.ModelAdmin):
    list_display = ('title', 'footer')

class GuideAdmin(admin.ModelAdmin):
    list_display = ('header', 'step_count')


admin.site.register(Jumbotron, JumbotronAdmin)
admin.site.register(Guide, GuideAdmin)
