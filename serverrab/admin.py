from django.contrib import admin
from .models import Admin,Worker,Client,Pristavka,Computers,Bar,Rooms,Orders,CompClub
class SomeDataAdmin(admin.ModelAdmin):
    list_display = ["name", "Phone_client"]
    search_fields = ["name", "Phone_client"]
admin.site.register(Admin)
admin.site.register(Worker)
admin.site.register(Client,SomeDataAdmin)
admin.site.register(Pristavka)
admin.site.register(Computers)
admin.site.register(Bar)
admin.site.register(Rooms)
admin.site.register(Orders)
admin.site.register(CompClub)


