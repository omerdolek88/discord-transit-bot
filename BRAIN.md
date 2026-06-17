# Brain — Geliştirme Notları

Bu dosya kullanıcıya değil, projeyi geliştirirken bana (ve Claude'a) yön vermek için. Kullanıcıya bakan açıklamalar README.md'de.

## Mevcut durum

- Tek dosya: [bot.py](bot.py) — discord.py + pyhafas (VSNProfile).
- Token `.env`'deki `DISCORD_TOKEN` değişkeninden okunuyor (`python-dotenv`), kod içinde sabit değil.
- Kullanıcıya dönen tüm mesajlar ve kod içi yorumlar Almanca — VSN bölgesindeki Discord kullanıcıları hedef kitle. Bu dili koru, Türkçe/İngilizce karıştırma.
- Komutlar: `!test`, `!tren <istasyon adı>`.
- `requirements.txt` henüz yok; README bundan bahsediyor ama dosya repoda mevcut değil.

## Bilinen eksikler

- `requirements.txt` eksik (discord.py, pyhafas, python-dotenv).
- Tek dosyada her şey var; büyürse (yeni komutlar, başka API'ler) modüllere bölünmeli.
- Hata yönetimi tek bir genel `except Exception` — API'ye özgü hata tipleri ayrılmamış.
- Test yok.

## Kararlar / nedenleri

- DB (Deutsche Bahn) HAFAS profili yerine VSNProfile kullanılıyor çünkü DB sunucusu kapalı/kararsızdı.
- Secrets `.env`'de tutuluyor, repoya commit edilmiyor (`.gitignore`'a `.env` eklendi).

## Sıradaki adımlar (henüz yapılmadı, fikir aşamasında)

- `requirements.txt` ekle.
