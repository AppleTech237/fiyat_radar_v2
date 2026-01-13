# FIYAT RADAR

## *Grup Adı:* Fiyat Radar Grubu

## Grup Üyeleri
- Jean Innocent Manta Nsangou  
- Gaius Joresse Azangue Tengam  
- Matias Fernando Ndong Owono  
- Mario Enrique Motede Dasilva  

## Projenin Amacı
Fiyat Radar, Django framework’ü kullanılarak geliştirilmiş bir web uygulamasıdır.  
Bu uygulama, kullanıcıların farklı marketlerde satılan ürünlerin fiyatlarını
kolayca karşılaştırabilmesini amaçlamaktadır.

Projenin temel hedefleri şunlardır:
- Fiyat karşılaştırmasını hızlı ve anlaşılır hale getirmek  
- Kullanıcıların daha ekonomik alışveriş yapmasına yardımcı olmak  
- Sade, modern, responsive ve kullanıcı dostu bir arayüz sunmak  
- Django tabanlı web uygulaması geliştirme becerilerini pekiştirmek  

## Kullanılan Teknolojiler
- Python 3.x  
- Django 4.x  
- HTML5  
- CSS3  
- SQLite (varsayılan veritabanı)

## Proje Yapısı
```text
fiyat_radar/
│
├── accounts/      → Kullanıcı yönetimi (login, register, user_profile)        
├── pages/         → Statik sayfalar (Home, About, Contact)      
├── products/      → Ürünler ve fiyat karşılaştırma işlemleri    
├── stores/        → Market listesi ve market detayları          
├── templates/     → base.html                                  
├── static/        → CSS, JS ve görseller                        
├── media/         → Yüklenen medya dosyaları                    
├── manage.py      → Django proje giriş noktası
└── README.md
```

## Fonksiyonlar

* Kullanıcı kayıt ve giriş sistemi
* Ürün listeleme
* Ürün detay sayfaları
* Farklı marketler arasında fiyat karşılaştırma
* Market listeleme ve detay görüntüleme
* Kullanıcı dostu ve sade arayüz


## Uygulama Sorumluları ve Görev Dağılımı

### Gaius Joresse Azangue Tengam
* alerts_form.html
* Ürün Listesi
* Ürün Detay Sayfaları
* Fiyat Karşılaştırma Sayfası
* Ürün Arama Sayfası
* Uyarı Sayfası
* Kullanıcı Deneyimi (UX) İyileştirmeleri

### Jean Innocent Manta Nsangou
* login.html
* register.html
* user_profile.html
* accounts/forms.py
* account/urls.py
* accounts/views.py
* stores/models.py
* stores/urls.py
* stores/views.py

## Matias Fernando Ndong Owono ve Mario Enrique Motede Dasilva
* Store_list.html
* about.html
* contact.html
* home.html
* pages/urls.py
* pages/views.py



## Sonuç
Fiyat Radarı projesi, bir üniversite çalışmasının parçası olarak geliştirilmiştir ve Django çerçevesini kullanarak web uygulaması geliştirme süreçlerini öğrenmeyi ve ekip çalışmasını teşvik etmeyi amaçlamaktadır.
Gerçek dünya sorununa çözüm sunan bu proje, kullanıcıların en iyi satın alımları yapmalarına yardımcı olur.

