# Insta Client #

[![instaclient](images/release-v1.0.0-red.svg)](https://github.com/hacernur/instaclient/releases/tag/v1.0.0)
![instaclient](images/license-MIT-yellowgreen.svg)

### **Proje Fikri**

Proje [Hipo](http://hipolabs.com/) firmasının 2015 yaz stajı için vermiş olduğu
proje ödevidir.

### **Proje Özellikleri**

* Aranılan hashtag'ta instagram'da profili açık hesaplardan 20 resim çekilip gösteriliyor.
* Resimler 3 farklı boyutta kullanıcıya gösterilebiliyor. (150x150, 320x320, 640x640)
* Çoklu dil desteği eklendi. (Türkçe, İngilizce)
* En son aranan ve en çok aranan 5 hashtag ekranda gösteriliyor link şeklinde.

### **Gelecekte Eklenecek Özellikler**

* Cinsel içerikli, argo kelimelerin en son ve en çok aranan hashtag'lerde gözükmesi engellenecek.
* Başka kullanıcılara resim desteği sağlanacak.

### **Projenin yerelde çalışır hale getirilmesi**

* virtualenv -p python3 InstaClient/env
* source env/bin/activate
* git clone https://github.com/hacernur/instaclient.git
* cd instaclient
* pip install -r requirements.txt


Not: Projenin görselinin düzgün gözükebilmesi için
static/lib/ dizini altına requirements.txt'de belirtilen
bootstrap, font-awesome, jquery kütüphanelerinin eklenemesi
gereklidir.

Not: Projenin yerelde çalışabilmesi için secret.py dosyasına 
ihtiyaç vardır. Bu dosya içerisinde SECRET_KEY bulunmaktadır.
Güvenlik sebebi ile bu anahtar değeri github'a atılmamıştır.
