from django.contrib import admin

# Register your models here.
from mysite_app.models import *
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject','email', 'status']
    list_editable = ['status']
    list_filter = ['status']
    search_fields = ('name', 'email')
    readonly_fields =('name', 'subject', 'email', 'message')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(About)
admin.site.register(MyInfo)
admin.site.register(Services)

admin.site.register(Portfolio)

admin.site.register(EducationDetail)
admin.site.register(ExprienceDetail)