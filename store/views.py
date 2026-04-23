from django.shortcuts import render, get_object_or_404
from .models import Produk, Banner
from .models import TentangKami
from .models import Artikel

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