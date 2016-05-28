# Insta Client #

## **Projenin yerelde çalışır hale getirilmesi**

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
