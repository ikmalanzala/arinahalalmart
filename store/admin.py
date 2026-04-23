from django.contrib import admin
from .models import Produk
from .models import Banner
from .models import TentangKami
from .models import SettingWebsite
from .models import Artikel

admin.site.register(Produk)
admin.site.register(Banner)
@admin.register(TentangKami)
class TentangKamiAdmin(admin.ModelAdmin):
    list_display = ('nama_toko',)


@admin.register(SettingWebsite)
class SettingWebsiteAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SettingWebsite.objects.exists()
    
@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('judul',)}
    list_display = ('judul', 'tanggal')