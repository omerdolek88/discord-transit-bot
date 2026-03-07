import discord
from discord.ext import commands
import datetime
from pyhafas import HafasClient
from pyhafas.profile import VSNProfile

# DB'nin kapalı sunucusu yerine çalışan alternatif VSN sunucusunu kullanıyoruz
hafas = HafasClient(VSNProfile())

# İZİNLER: Botun mesajları okuması için gereken kritik ayar
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'>>> Başarıyla giriş yapıldı: {bot.user.name}')
    print('>>> API entegrasyonu aktif, komutlar dinleniyor!')

@bot.command()
async def test(ctx):
    await ctx.send('Merhaba! Sistem tıkır tıkır çalışıyor 🚀')

@bot.command()
async def tren(ctx, *, istasyon_adi: str):
    await ctx.send(f"🚉 `{istasyon_adi}` için canlı veriler çekiliyor, bir saniye...")
    
    try:
        locations = hafas.locations(istasyon_adi)
        if not locations:
            await ctx.send("❌ İstasyon bulunamadı. Lütfen adını doğru yazdığından emin ol.")
            return
            
        istasyon = locations[0]
        
        departures = hafas.departures(
            station=istasyon,
            date=datetime.datetime.now(),
            max_trips=5
        )
        
        if not departures:
            await ctx.send("🤷‍♂️ Yakın zamanda planlanmış bir sefer bulunamadı.")
            return

        mesaj = f"🚆 **{istasyon.name}** Anlık Kalkış Tablosu:\n\n"
        for dep in departures:
            saat = dep.dateTime.strftime("%H:%M")
            hat = dep.name
            yon = dep.direction
            gecikme = ""
            
            if dep.delay and dep.delay.total_seconds() > 0:
                gecikme_dk = int(dep.delay.total_seconds() / 60)
                gecikme = f" (🔴 +{gecikme_dk} dk rötar)"
            
            mesaj += f"• **{saat}** | {hat} ➡️ {yon}{gecikme}\n"
        
        await ctx.send(mesaj)
        
    except Exception as e:
        await ctx.send(f"⚠️ Veri çekilirken bir hata oluştu: {e}")

# DİKKAT: TOKEN'INI BURAYA GİRMEYİ UNUTMA
TOKEN = 'DEIN_DISCORD_BOT_TOKEN_HIER'
if __name__ == '__main__':
    bot.run(TOKEN)