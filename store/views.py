from django.shortcuts import render, get_object_or_404
from .models import Produk, Banner
from .models import TentangKami
from .models import Artikel
from .models import Testimoni
def home(request):
    produk = Produk.objects.all()
    banner = Banner.objects.filter(aktif=True)

    return render(request, 'index.html', {
        'produk': produk,
        'banner': banner
    })

def detail_produk(request, id):
    produk = get_object_or_404(Produk, id=id)
    return render(request, 'detail.html', {'produk': produk})
def tentang(request):
    data = TentangKami.objects.first()
    return render(request, 'tentang.html', {'data': data})

def artikel_list(request):
    data = Artikel.objects.all().order_by('-tanggal')
    return render(request, 'artikel_list.html', {'artikel': data})

def artikel_detail(request, slug):
    data = Artikel.objects.get(slug=slug)
    return render(request, 'artikel_detail.html', {'data': data})

def home(request):

    produk = Produk.objects.all()[:3]

    return render(request, 'index.html', {
        'produk': produk
    })

def katalog(request):

    produk = Produk.objects.all()

    return render(request, 'katalog.html', {
        'produk': produk
    })

def home(request):

    produk = Produk.objects.all()[:3]
    banner = Banner.objects.all()

    return render(request, 'index.html', {
        'produk': produk,
        'banner': banner,
    })

def testimoni(request):

    data_testimoni = Testimoni.objects.all()

    return render(request, 'testimoni.html', {
        'testimoni': data_testimoni
    })