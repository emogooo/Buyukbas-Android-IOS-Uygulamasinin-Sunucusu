from django.db import models
"""
from django.db.models import signals
from django.dispatch import receiver
from django.db.models.signals import pre_save
"""
class Asi(models.Model):
    ad = models.CharField(max_length=30)
    aciklama = models.CharField(max_length=200)

    def __str__(self):
        return self.ad

class CikisSebebi(models.Model):
    ad = models.CharField(max_length=30)

    def __str__(self):
        return self.ad

class Isletme(models.Model):
    ad = models.CharField(max_length=30)

    def __str__(self):
        return self.ad

class Cinsiyet(models.Model):
    ad = models.CharField(max_length=30)

    def __str__(self):
        return self.ad

class Irk(models.Model):
    ad = models.CharField(max_length=30)

    def __str__(self):
        return self.ad

class Pazarlikci(models.Model):
    ad = models.CharField(max_length=30)
    soyad = models.CharField(max_length=30)
    telefon = models.CharField(max_length=11)
    adres = models.CharField(max_length=70)

    def __str__(self):
        return self.ad + " " + self.soyad

class AlisBilgisi(models.Model):
    fiyatTL = models.PositiveSmallIntegerField()
    tarih = models.DateField(auto_now=False, auto_now_add=False)
    kilo = models.PositiveSmallIntegerField()
    pazarlikci = models.ForeignKey(Pazarlikci, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fiyatTL) + " " + str(self.kilo) + " " + str(self.tarih) + " " + str(self.pazarlikci)

class Hayvan(models.Model):
    kupeNo = models.CharField(max_length=10)
    padokNo = models.CharField(max_length=10)
    aciklama = models.CharField(max_length=200)
    aktif = models.BooleanField(default=True)
    alisBilgisi = models.ForeignKey(AlisBilgisi, on_delete=models.CASCADE)
    irk = models.ForeignKey(Irk, on_delete=models.CASCADE)
    cinsiyet = models.ForeignKey(Cinsiyet, on_delete=models.CASCADE)
    isletme = models.ForeignKey(Isletme, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.kupeNo)

class AsiBilgi(models.Model):
    hayvan = models.ForeignKey(Hayvan, on_delete=models.CASCADE)
    asi = models.ForeignKey(Asi, on_delete=models.CASCADE)
    tarih = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.hayvan) + " " +str(self.asi)

class Cikis(models.Model):
    sebep = models.ForeignKey(CikisSebebi, on_delete=models.CASCADE)
    hayvan = models.ForeignKey(Hayvan, on_delete=models.CASCADE)
    tarih = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.hayvan) + " " + str(self.sebep)

class Ticaret(models.Model):
    cikis = models.ForeignKey(Cikis, on_delete=models.CASCADE)
    musteri = models.ForeignKey(Pazarlikci, on_delete=models.CASCADE)
    fiyatTL = models.PositiveSmallIntegerField()
    tarih = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.musteri) + " " + str(self.cikis) + " " + str(self.fiyatTL)

class EskiKupeNo(models.Model):
    hayvan = models.ForeignKey(Hayvan, on_delete=models.CASCADE)
    eskiKupe = models.CharField(max_length=10)
    yeniKupe = models.CharField(max_length=10)
    tarih = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.hayvan) + " " + str(self.eskiKupe) + " " + str(self.yeniKupe)

"""
@receiver(signals.pre_save, sender=Hayvan)
def createOrUpdate(sender, instance, **kwargs):
    if kwargs['created']:
        print('created')
    else:
       print('updated')

pre_save.connect(createOrUpdate, sender=Hayvan)
"""