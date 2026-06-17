# Discord Transit Bot

VSN (Verkehrsverbund Süd-Niedersachsen) toplu taşıma ağındaki istasyonlar için canlı kalkış bilgisi veren basit bir Discord botu. [pyhafas](https://github.com/FahrPlaner/pyHaFAS) üzerinden HAFAS API'sine bağlanır.

## Komutlar

- `!test` — botun çalıştığını doğrular.
- `!tren <istasyon adı>` — verilen istasyonun sonraki 5 kalkışını (saat, hat, yön, varsa rötar) listeler.

## Kurulum

```bash
git clone git@github.com:omerdolek88/discord-transit-bot.git
cd discord-transit-bot
python3 -m venv venv
source venv/bin/activate
pip install discord.py pyhafas
```

[bot.py](bot.py) içindeki `TOKEN` değişkenine kendi Discord bot token'ını gir, ardından çalıştır:

```bash
python bot.py
```

Bot'un mesaj içeriğini okuyabilmesi için Discord Developer Portal'da **Message Content Intent**'in açık olması gerekir.
