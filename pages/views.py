from django.shortcuts import render
from .models import Category, KaravanModel, RandevuModel, YorumModel

# Create your views here.

def IndexView(request):
    karavan = KaravanModel.objects.filter(is_home=True)
    category = Category.objects.all()
    yorum = YorumModel.objects.all()

    context = {
        'karavan' : karavan,
        'category' : category,
        'yorum' : yorum
    }

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        telefon = request.POST['tel']
        konu = request.POST['konu']
        mesaj = request.POST['mesaj']

        mesajkayit = RandevuModel(name=username, email=email, telefon=telefon, konu=konu, mesaj=mesaj)
        mesajkayit.save()
        return render(request, 'pages/randevu.html', {'kayit' : 'Randevunuz başarılı bir şekilde oluşturuldu. Sizinle irtibata geçeceğiz.'})
    else:

        return render(request, 'pages/index.html', context)

def AboutView(request):
    return render(request, 'pages/about.html')

def ContactView(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        telefon = request.POST['tel']
        konu = request.POST['konu']
        mesaj = request.POST['mesaj']

        mesajkayit = RandevuModel(name=username, email=email, telefon=telefon, konu=konu, mesaj=mesaj )
        mesajkayit.save()

        return render(request, 'pages/contact.html', {'kayit' : 'İletişim bilgileriniz başarılı bir şekilde kaydedildi. Lütfen size ulaşmamızı bekleyiniz.'})
    else:

        return render(request, 'pages/contact.html')

def ModelView(request):
    karavan = KaravanModel.objects.all()
    category = Category.objects.all()

    context = {
        'karavan' : karavan,
        'category' : category
    }
    return render(request, 'pages/model.html', context)

def ModelDetailView(request, slug):
    karavan = KaravanModel.objects.get(slug=slug)
    category = Category.objects.all()

    context = {
        'karavan' : karavan,
        'category' : category
    }

    return render(request, 'pages/model_detail.html', context)

def CategoryView(request, category_slug):
    karavan = KaravanModel.objects.filter(category__slug=category_slug)
    category = Category.objects.all()

    context = {
        'karavan' : karavan,
        'category' : category
    }

    return render(request, 'pages/model.html', context)

def RandevuView(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        telefon = request.POST['tel']
        konu = request.POST['konu']
        mesaj = request.POST['mesaj']

        mesajkayit = RandevuModel(name=username, email=email, telefon=telefon, konu=konu, mesaj=mesaj)
        mesajkayit.save()
        return render(request, 'pages/randevu.html', {'kayit' : 'Randevunuz başarılı bir şekilde oluşturuldu. Sizinle irtibata geçeceğiz.'})

    else:

        return render(request, 'pages/randevu.html')



