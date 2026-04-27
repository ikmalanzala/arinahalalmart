from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from .models import Produk, Banner, TentangKami, SettingWebsite, Artikel

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga')
    search_fields = ('nama',)
    list_filter = ('harga',)
    ordering = ('-id',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('judul', 'aktif')
    list_filter = ('aktif',)
    search_fields = ('judul',)


@admin.register(TentangKami)
class TentangKamiAdmin(admin.ModelAdmin):
    list_display = ('nama_toko',)


@admin.register(SettingWebsite)
class SettingWebsiteAdmin(admin.ModelAdmin):
    list_display = ('nama_toko', 'nomor_wa')

    def has_add_permission(self, request):
        return not SettingWebsite.objects.exists()


@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal')
    search_fields = ('judul',)
    prepopulated_fields = {'slug': ('judul',)}
    ordering = ('-tanggal',)

    