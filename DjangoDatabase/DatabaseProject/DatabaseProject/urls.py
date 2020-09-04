from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Database import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^ekle/isletme/', views.isletmeEkle),
    url(r'^ekle/asi/', views.asiEkle),
    url(r'^ekle/cikissebebi/', views.cikisSebebiEkle),
    url(r'^ekle/cinsiyet/', views.cinsiyetEkle),
    url(r'^ekle/irk/', views.irkEkle),
    url(r'^ekle/pazarlikci/', views.pazarlikciEkle),
    url(r'^ekle/alisBilgisi/', views.alisBilgisiEkle),
    url(r'^ekle/hayvan/', views.hayvanEkle),
    url(r'^ekle/asibilgisi/', views.asiBilgisiEkle),
    url(r'^ekle/cikis/', views.cikisEkle),
    url(r'^ekle/ticaret/', views.ticaretEkle),
    url(r'^ekle/eskikupeno/', views.eskiKupeNoEkle),
    url(r'^sil/isletme/', views.isletmeSil),
    url(r'^sil/asi/', views.asiSil),
    url(r'^sil/cikissebebi/', views.cikisSebebiSil),
    url(r'^sil/cinsiyet/', views.cinsiyetSil),
    url(r'^sil/irk/', views.irkSil),
    url(r'^sil/pazarlikci/', views.pazarlikciSil),
    url(r'^sil/alisBilgisi/', views.alisBilgisiSil),
    url(r'^sil/hayvan/', views.hayvanSil),
    url(r'^sil/asibilgisi/', views.asiBilgisiSil),
    url(r'^sil/cikis/', views.cikisSil),
    url(r'^sil/ticaret/', views.ticaretSil),
    url(r'^sil/eskikupeno/', views.eskiKupeNoSil),
    url(r'^guncelle/isletme/', views.isletmeGuncelle),
    url(r'^guncelle/asi/', views.asiGuncelle),
    url(r'^guncelle/cikissebebi/', views.cikisSebebiGuncelle),
    url(r'^guncelle/cinsiyet/', views.cinsiyetGuncelle),
    url(r'^guncelle/irk/', views.irkGuncelle),
    url(r'^guncelle/pazarlikci/', views.pazarlikciGuncelle),
    url(r'^guncelle/alisbilgisi/', views.alisBilgisiGuncelle),
    url(r'^guncelle/hayvan/', views.hayvanGuncelle),
    url(r'^guncelle/asibilgisi/', views.asiBilgisiGuncelle),
    url(r'^guncelle/cikis/', views.cikisGuncelle),
    url(r'^guncelle/ticaret/', views.ticaretGuncelle),
    url(r'^guncelle/eskikupeno/', views.eskiKupeNoGuncelle)
]

