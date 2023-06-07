# Pyton_SQLİTE_EXAPMLES
Veritabanı Yapısı
## Veritabanı Yapısı

Bu projede kullanılan SQLite veritabanı, aşağıdaki tabloları ve ilişkileri içerir:

### Tablo 1: Kullanıcılar (personel)
CREATE TABLE IF NOT EXISTS personel (
  isim TEXT,
  soyisim TEXT,
  departman TEXT,
  maas INT
);
Bu veritabanı yapısı, projenizin gereksinimlerine ve verilerinizi nasıl organize etmek istediğinize bağlı olarak değişebilir. Yukarıdaki örnek tablolar, temel bir veritabanı yapısı sağlamaktadır, ancak projenizin özel gereksinimlerini ve ilişkilerini göz önünde bulundurarak tabloları ve sütunları özelleştirebilirsiniz.
import sqlite3

 Veritabanı bağlantısı oluşturma
conn = sqlite3.connect('veritabani.db')
cursor = conn.cursor()

 Veri ekleme işlemi
sql = "INSERT INTO personel VALUES('SABRİ', 'elmastas', 'Bilgi Güvenligi', 40000)"
cursor.execute(sql)

 Veritabanı üzerinde değişiklikleri kaydetme
conn.commit()

Bağlantıyı kapatma
conn.close()

Bu örnekler, SQLite veritabanında kullanabileceğiniz bazı sorguları göstermektedir. İhtiyaçlarınıza göre bu sorguları değiştirebilir veya geliştirebilirsiniz.
