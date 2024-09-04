# WebCookieLogger

## Açıklama

WebCookieLogger, tarayıcı çerezlerini toplamak için kullanılan bir Python tabanlı HTTP sunucusudur. Bu proje, güvenlik testleri ve eğitim amaçlı olarak geliştirilmiştir. Kod, yalnızca izinli ortamlarda ve yasal sınırlar içinde kullanılmalıdır.

Bu proje, bir HTTP sunucusu kurarak çerezleri toplar ve bu bilgileri belirtilen bir URL'ye gönderir. Çerez toplama işlemi izinsiz kişisel veri toplama anlamına gelebilir ve yasal sonuçlar doğurabilir.

## Özellikler

- **HTTP Sunucusu:** Basit bir HTTP sunucusu kurar ve GET isteklerini dinler.
- **Public URL Oluşturma:** `serveo.net` kullanarak geçici bir public URL oluşturur.
- **Çerez Toplama:** Oluşturulan URL'yi kullanarak çerezleri hedef URL'ye gönderir.
- **JavaScript Enjeksiyonu:** Oluşturulan URL'yi JavaScript kodu ile hedef tarayıcıya enjekte eder.

## Kullanım

1. **Sunucuyu Başlatın:**

   ```bash
   python getcookies.py
