from django.contrib import admin
from .models import Register,jobpro,jobseek,jobselection

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','password')

class jobproAdmin(admin.ModelAdmin):
    list_display = ('id','location1','jobdes','jobimg','relation')

class jobseekAdmin(admin.ModelAdmin):
    list_display = ('location2','relation2')

class jobselectionAdmin(admin.ModelAdmin):
    list_display = ('jobdes','relation3')
# Register your models here.

admin.site.register(Register,RegisterAdmin)
admin.site.register(jobpro,jobproAdmin)
admin.site.register(jobseek,jobseekAdmin)
admin.site.register(jobselection,jobselectionAdmin)