from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CikisSebebi,EskiKupeNo,AsiBilgi,Cinsiyet,Pazarlikci,AlisBilgisi,Ticaret,Isletme,Cikis,Asi,Irk,Hayvan
import json

@api_view(["POST"])
def isletmeEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        ad = str(veriler.get('ad'))
        isletme = Isletme(ad = ad)
        isletme.save()
        return JsonResponse("Kayit yapildi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def asiEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        ad = str(veriler.get('ad'))
        aciklama = str(veriler.get('aciklama'))
        asi = Asi(ad = ad, aciklama = aciklama)
        asi.save()
        return JsonResponse("Kayit yapildi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def cikisSebebiEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        ad = str(veriler.get('ad'))
        cikisSebebi = CikisSebebi(ad = ad)
        cikisSebebi.save()
        return JsonResponse("Kayit yapildi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def cinsiyetEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        ad = str(veriler.get('ad'))
        cinsiyet = Cinsiyet(ad = ad)
        cinsiyet.save()
        return JsonResponse("Kayit yapildi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def irkEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        ad = str(veriler.get('ad'))
        irk = Irk(ad = ad)
        irk.save()
        return JsonResponse("Kayit yapildi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def pazarlikciEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        ad = str(veriler.get('ad'))
        soyad = str(veriler.get('soyad'))
        telefon = str(veriler.get('telefon'))
        adres = str(veriler.get('adres'))
        pazarlikci = Pazarlikci(ad = ad, soyad = soyad, telefon = telefon, adres = adres)
        pazarlikci.save()
        return JsonResponse("Pazarlikci eklendi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def alisBilgisiEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        fiyatTL = int(veriler.get('fiyatTL'))
        tarih = str(veriler.get('tarih'))
        kilo = int(veriler.get('kilo'))
        pazarlikciNo = int(veriler.get('pazarlikci'))
        pazarlikci = Pazarlikci.objects.get(pk = pazarlikciNo)
        alisBilgisi = AlisBilgisi(fiyatTL = fiyatTL, tarih = tarih, kilo = kilo, pazarlikci = pazarlikci)
        alisBilgisi.save()
        return JsonResponse("Alis bilgisi eklendi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def hayvanEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        kupeNo = str(veriler.get('kupeNo'))
        padokNo = str(veriler.get('padokNo'))
        aciklama = str(veriler.get('aciklama'))
        aktif = bool(veriler.get('aktif'))
        alisBilgisiNo = int(veriler.get('alisBilgisi'))
        alisBilgisi = AlisBilgisi.objects.get(pk = alisBilgisiNo)
        irkNo = int(veriler.get('irk'))
        irk = Irk.objects.get(pk = irkNo)
        cinsiyetNo = int(veriler.get('cinsiyet'))
        cinsiyet = Cinsiyet.objects.get(pk = cinsiyetNo)
        isletmeNo = int(veriler.get('isletme'))
        isletme = Isletme.objects.get(pk = isletmeNo)
        hayvan = Hayvan(kupeNo = kupeNo, padokNo = padokNo, aciklama = aciklama, aktif = aktif, alisBilgisi = alisBilgisi, irk = irk, cinsiyet = cinsiyet, isletme = isletme)
        hayvan.save()
        return JsonResponse("Hayvan bilgisi eklendi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def asiBilgisiEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        hayvanNo = int(veriler.get('hayvan'))
        hayvan = Hayvan.objects.get(pk = hayvanNo)
        asiNo = int(veriler.get('asi'))
        asi = Asi.objects.get(pk = asiNo)
        tarih = str(veriler.get('tarih'))
        asiBilgisi = AsiBilgi(hayvan = hayvan, asi = asi, tarih = tarih)
        asiBilgisi.save()
        return JsonResponse("AsiBilgisi bilgisi eklendi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def cikisEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        sebepNo = int(veriler.get('sebep'))
        sebep = CikisSebebi.objects.get(pk = sebepNo)
        hayvanNo = int(veriler.get('hayvan'))
        hayvan = Hayvan.objects.get(pk = hayvanNo)
        tarih = str(veriler.get('tarih'))
        cikis = Cikis(sebep = sebep, hayvan = hayvan, tarih = tarih)
        cikis.save()
        return JsonResponse("Cikis bilgisi eklendi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def ticaretEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        cikisNo = int(veriler.get('cikis'))
        cikis = Cikis.objects.get(pk = cikisNo)
        musteriNo = int(veriler.get('musteri'))
        musteri = Pazarlikci.objects.get(pk = musteriNo)
        fiyatTL = int(veriler.get('fiyatTL'))
        tarih = str(veriler.get('tarih'))
        ticaret = Ticaret(cikis = cikis, musteri = musteri, fiyatTL = fiyatTL, tarih = tarih)
        ticaret.save()
        return JsonResponse("Ticaret bilgisi eklendi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def eskiKupeNoEkle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        hayvanNo = int(veriler.get('hayvan'))
        hayvan = Hayvan.objects.get(pk = hayvanNo)
        eskiKupe = str(veriler.get('eskiKupe'))
        yeniKupe= str(veriler.get('yeniKupe'))
        tarih = str(veriler.get('tarih'))
        eskiKupeNo = EskiKupeNo(hayvan = hayvan, eskiKupe = eskiKupe, yeniKupe = yeniKupe, tarih = tarih)
        eskiKupeNo.save()
        return JsonResponse("Eski kupe bilgisi eklendi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def isletmeSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        isletme = Isletme.objects.get(pk = id)
        isletme.delete()
        return JsonResponse("Isletme silindi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def asiSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        asi = Asi.objects.get(pk = id)
        asi.delete()
        return JsonResponse("Asi silindi", safe = False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def cikisSebebiSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        cikisSebebi = CikisSebebi.objects.get(pk=id)
        cikisSebebi.delete()
        return JsonResponse("Cikis sebebi silindi", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def cinsiyetSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        cinsiyet = Cinsiyet.objects.get(pk=id)
        cinsiyet.delete()
        return JsonResponse("Cinsiyet silindi", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def irkSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        irk = Irk.objects.get(pk=id)
        irk.delete()
        return JsonResponse("Irk silindi", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def pazarlikciSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        pazarlikci = Pazarlikci.objects.get(pk=id)
        pazarlikci.delete()
        return JsonResponse("Pazarlikci silindi", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def alisBilgisiSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        alisBilgisi = AlisBilgisi.objects.get(pk=id)
        alisBilgisi.delete()
        return JsonResponse("Alis bilgisi silindi", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def hayvanSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        hayvan = Hayvan.objects.get(pk=id)
        hayvan.delete()
        return JsonResponse("Hayvan silindi", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def asiBilgisiSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        asiBilgisi = AsiBilgi.objects.get(pk=id)
        asiBilgisi.delete()
        return JsonResponse("Asi bilgisi silindi", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def cikisSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        cikis = Cikis.objects.get(pk=id)
        cikis.delete()
        return JsonResponse("Cikis silindi", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def ticaretSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        ticaret = Ticaret.objects.get(pk=id)
        ticaret.delete()
        return JsonResponse("Ticaret silindi", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def eskiKupeNoSil(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        eskiKupeNo = EskiKupeNo.objects.get(pk=id)
        eskiKupeNo.delete()
        return JsonResponse("Eski kupe silindi", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def isletmeGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        isletme = Isletme.objects.get(pk = id)
        guncellenecekAd = str(veriler.get('ad'))
        if not guncellenecekAd == "None" and not guncellenecekAd == "":
            isletme.ad = guncellenecekAd
            isletme.save()
            return JsonResponse("Isletme guncellendi", safe = False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def asiGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        asi = Asi.objects.get(pk = id)
        guncellenecekAd = str(veriler.get('ad'))
        if not guncellenecekAd == "None" and not guncellenecekAd == "":
            asi.ad = guncellenecekAd
            asi.save()
            return JsonResponse("Asi guncellendi", safe = False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def cikisSebebiGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        cikisSebebi = CikisSebebi.objects.get(pk = id)
        guncellenecekAd = str(veriler.get('ad'))
        if not guncellenecekAd == "None" and not guncellenecekAd == "":
            cikisSebebi.ad = guncellenecekAd
            cikisSebebi.save()
            return JsonResponse("Cikis Sebebi guncellendi", safe = False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def cinsiyetGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        cinsiyet = Cinsiyet.objects.get(pk = id)
        guncellenecekAd = str(veriler.get('ad'))
        if not guncellenecekAd == "None" and not guncellenecekAd == "":
            cinsiyet.ad = guncellenecekAd
            cinsiyet.save()
            return JsonResponse("Cinsiyet guncellendi", safe = False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def irkGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        irk = Irk.objects.get(pk = id)
        guncellenecekAd = str(veriler.get('ad'))
        if not guncellenecekAd == "None" and not guncellenecekAd == "":
            irk.ad = guncellenecekAd
            irk.save()
            return JsonResponse("Irk guncellendi", safe = False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def pazarlikciGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        pazarlikci = Pazarlikci.objects.get(pk = id)
        guncellenecekAd = str(veriler.get('ad'))
        guncellenecekSoyad = str(veriler.get('soyad'))
        guncellenecekAdres = str(veriler.get('adres'))
        guncellenecekTelefon = str(veriler.get('telefon'))
        kontrol = False
        if not guncellenecekAd == "None" and not guncellenecekAd == "":
            pazarlikci.ad = guncellenecekAd
            kontrol = True
        if not guncellenecekSoyad == "None" and not guncellenecekSoyad == "":
            pazarlikci.soyad = guncellenecekSoyad
            kontrol = True
        if not guncellenecekAdres == "None" and not guncellenecekAdres == "":
            pazarlikci.adres = guncellenecekAdres
            kontrol = True
        if not guncellenecekTelefon == "None" and not guncellenecekTelefon == "":
            pazarlikci.telefon = guncellenecekTelefon
            kontrol = True
        if kontrol:
            pazarlikci.save()
            return JsonResponse("Pazarlikci guncellendi", safe=False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def alisBilgisiGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        alisBilgisi = AlisBilgisi.objects.get(pk = id)
        guncellenecekFiyatTL = str(veriler.get('fiyatTL'))
        guncellenecekTarih = str(veriler.get('tarih'))
        guncellenecekKilo = str(veriler.get('kilo'))
        guncellenecekPazarlikciNo = str(veriler.get('pazarlikci'))
        kontrol = False
        if not guncellenecekFiyatTL == "None" and not guncellenecekFiyatTL == "":
            guncellenecekFiyatTL = int(guncellenecekFiyatTL)
            alisBilgisi.fiyatTL = guncellenecekFiyatTL
            kontrol = True
        if not guncellenecekTarih == "None" and not guncellenecekTarih == "":
            alisBilgisi.tarih = guncellenecekTarih
            kontrol = True
        if not guncellenecekKilo == "None" and not guncellenecekKilo == "":
            guncellenecekKilo = int(guncellenecekKilo)
            alisBilgisi.kilo = guncellenecekKilo
            kontrol = True
        if not guncellenecekPazarlikciNo == "None" and not guncellenecekPazarlikciNo == "":
            guncellenecekPazarlikciNo = int(guncellenecekPazarlikciNo)
            guncellenecekPazarlikci = Pazarlikci.objects.get(pk = guncellenecekPazarlikciNo)
            alisBilgisi.pazarlikci = guncellenecekPazarlikci
            kontrol = True
        if kontrol:
            alisBilgisi.save()
            return JsonResponse("Alis Bilgisi guncellendi", safe=False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def hayvanGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        hayvan = Hayvan.objects.get(pk = id)
        kupeNo = str(veriler.get('kupeno'))
        padokNo = str(veriler.get('padakno'))
        aciklama = str(veriler.get('aciklama'))
        aktif = str(veriler.get('aktif'))
        alisBilgisiNo = str(veriler.get('alisbilgisi'))
        irkNo = str(veriler.get('irk'))
        cinsiyetNo = str(veriler.get('cinsiyet'))
        isletmeNo = str(veriler.get('isletme'))
        kontrol = False
        if not kupeNo == "None" and not kupeNo == "":
            hayvan.kupeNo = kupeNo
            kontrol = True
        if not padokNo == "None" and not padokNo == "":
            hayvan.padokNo = padokNo
            kontrol = True
        if not aciklama == "None" and not aciklama == "":
            hayvan.aciklama = aciklama
            kontrol = True
        if not aktif == "None" and not aktif == "":
            aktif = bool(aktif)
            hayvan.aktif = aktif
            kontrol = True
        if not alisBilgisiNo == "None" and not alisBilgisiNo == "":
            alisBilgisiNo = int(alisBilgisiNo)
            alisBilgisi = AlisBilgisi.objects.get(pk = alisBilgisiNo)
            hayvan.alisBilgisi = alisBilgisi
            kontrol = True
        if not irkNo == "None" and not irkNo == "":
            irkNo = int(irkNo)
            irk = Irk.objects.get(pk = irkNo)
            hayvan.irk = irk
            kontrol = True
        if not cinsiyetNo == "None" and not cinsiyetNo == "":
            cinsiyetNo = int(cinsiyetNo)
            cinsiyet = Cinsiyet.objects.get(pk = cinsiyetNo)
            hayvan.cinsiyet = cinsiyet
            kontrol = True
        if not isletmeNo == "None" and not isletmeNo == "":
            isletmeNo = int(isletmeNo)
            isletme = Isletme.objects.get(pk = isletmeNo)
            hayvan.isletme = isletme
            kontrol = True
        if kontrol:
            hayvan.save()
            return JsonResponse("Hayvan guncellendi", safe=False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def asiBilgisiGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        asiBilgisi = AsiBilgi.objects.get(pk = id)
        hayvanNo = str(veriler.get('hayvan'))
        asiNo = str(veriler.get('asi'))
        tarih = str(veriler.get('tarih'))
        kontrol = False
        if not hayvanNo == "None" and not hayvanNo == "":
            hayvanNo = int(hayvanNo)
            hayvan = Hayvan.objects.get(pk = hayvanNo)
            asiBilgisi.hayvan = hayvan
            kontrol = True
        if not asiNo == "None" and not asiNo == "":
            asiNo = int(asiNo)
            asi = Asi.objects.get(pk = asiNo)
            asiBilgisi.asi = asi
            kontrol = True
        if not tarih == "None" and not tarih == "":
            asiBilgisi.tarih = tarih
            kontrol = True
        if kontrol:
            asiBilgisi.save()
            return JsonResponse("Asi Bilgisi guncellendi", safe=False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def cikisGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        cikis = Cikis.objects.get(pk = id)
        sebepNo = str(veriler.get('sebep'))
        hayvanNo = str(veriler.get('hayvan'))
        tarih = str(veriler.get('tarih'))
        kontrol = False
        if not sebepNo == "None" and not sebepNo == "":
            sebepNo = int(sebepNo)
            sebep = CikisSebebi.objects.get(pk = sebepNo)
            cikis.sebep = sebep
            kontrol = True
        if not hayvanNo == "None" and not hayvanNo == "":
            hayvanNo = int(hayvanNo)
            hayvan = Hayvan.objects.get(pk = hayvanNo)
            cikis.hayvan = hayvan
            kontrol = True
        if not tarih == "None" and not tarih == "":
            cikis.tarih = tarih
            kontrol = True
        if kontrol:
            cikis.save()
            return JsonResponse("Cikis guncellendi", safe=False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def ticaretGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        ticaret = Ticaret.objects.get(pk = id)
        cikisNo = str(veriler.get('cikis'))
        pazarlikciNo = str(veriler.get('musteri'))
        fiyatTL = str(veriler.get('fiyatTL'))
        tarih = str(veriler.get('tarih'))
        kontrol = False
        if not cikisNo == "None" and not cikisNo == "":
            cikisNo = int(cikisNo)
            cikis = Cikis.objects.get(pk = cikisNo)
            ticaret.cikis = cikis
            kontrol = True
        if not pazarlikciNo == "None" and not pazarlikciNo == "":
            pazarlikciNo = int(pazarlikciNo)
            pazarlikci = Pazarlikci.objects.get(pk = pazarlikciNo)
            ticaret.musteri = pazarlikci
            kontrol = True
        if not fiyatTL == "None" and not fiyatTL == "":
            fiyatTL = int(fiyatTL)
            ticaret.fiyatTL = fiyatTL
            kontrol = True
        if not tarih == "None" and not tarih == "":
            cikis.tarih = tarih
            kontrol = True
        if kontrol:
            cikis.save()
            return JsonResponse("Ticaret guncellendi", safe=False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def eskiKupeNoGuncelle(jsonDosyasi):
    try:
        veriler = json.loads(jsonDosyasi.body)
        id = int(veriler.get('id'))
        eskiKupeNo = EskiKupeNo.objects.get(pk = id)
        eskiKupe = str(veriler.get('cikis'))
        yeniKupe = str(veriler.get('musteri'))
        tarih = str(veriler.get('tarih'))
        kontrol = False
        if not eskiKupe == "None" and not eskiKupe == "":
            eskiKupeNo.eskiKupe = eskiKupe
            kontrol = True
        if not yeniKupe == "None" and not yeniKupe == "":
            eskiKupeNo.yeniKupe = yeniKupe
            kontrol = True
        if not tarih == "None" and not tarih == "":
            eskiKupeNo.tarih = tarih
            kontrol = True
        if kontrol:
            eskiKupeNo.save()
            return JsonResponse("Eski kupe numarasi guncellendi", safe=False)
        else:
            return JsonResponse("Duzgun deger gir", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_204_NO_CONTENT)
