from django.contrib import admin
from auto.models import TestConfig,Result,chassisConfig,neighborhoodConfig,Template,cpsTest,udpTest,ccTest,tpsTest,httpTest



class TestConfigAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(TestConfig,TestConfigAdmin)



class chassisConfigAdmin(admin.ModelAdmin):
    list_display = ('name','ip',)

admin.site.register(chassisConfig,chassisConfigAdmin)

class neighborhoodConfigAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(neighborhoodConfig,neighborhoodConfigAdmin)

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Template,TemplateAdmin)

class cpsTestAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(cpsTest,cpsTestAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('name','status','type','result',)

admin.site.register(Result,ResultAdmin)

admin.site.register(udpTest)
admin.site.register(ccTest)
admin.site.register(tpsTest)
admin.site.register(httpTest)
