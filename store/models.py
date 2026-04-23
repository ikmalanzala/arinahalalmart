from django.db import models
class Produk(models.Model):
    nama = models.CharField(max_length=200)
    harga = models.IntegerField()
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='produk/', blank=True, null=True)

    def __str__(self):
        return self.nama
class Banner(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    gambar = models.ImageField(upload_to='banner/')
    aktif = models.BooleanField(default=True)

    def __str__(self):
        return self.judul
    
class TentangKami(models.Model):
    nama_toko = models.CharField(max_length=100)
    deskripsi = models.TextField()
    keunggulan = models.TextField(help_text="Pisahkan dengan enter per poin")
    whatsapp = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_toko
    
class SettingWebsite(models.Model):
    nama_toko = models.CharField(max_length=100)
    nomor_wa = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    favicon = models.ImageField(upload_to='favicon/', blank=True, null=True)
    def __str__(self):
        return "Setting Website"
class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    konten = models.TextField()
    gambar = models.ImageField(upload_to='artikel/', blank=True, null=True)
    tanggal = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.judul