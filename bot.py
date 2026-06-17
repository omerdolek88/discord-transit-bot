import os
import datetime

import discord
from discord.ext import commands
from dotenv import load_dotenv
from pyhafas import HafasClient
from pyhafas.profile import VSNProfile

# Token wird aus der .env-Datei geladen, damit er nicht im Quellcode steht.
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Statt des abgeschalteten DB-Servers nutzen wir das stabile VSN-Profil.
hafas = HafasClient(VSNProfile())

# Berechtigungen: notwendig, damit der Bot Nachrichteninhalte lesen kann.
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f">>> Erfolgreich angemeldet als: {bot.user.name}")
    print(">>> API-Integration aktiv, Befehle werden empfangen.")


@bot.command()
async def test(ctx):
    """Einfacher Statusbefehl, um zu prüfen, ob der Bot online ist."""
    await ctx.send("Der Bot ist online und funktioniert einwandfrei.")


@bot.command()
async def tren(ctx, *, station_name: str):
    """Ruft die nächsten Abfahrten für einen angegebenen Bahnhof ab."""
    await ctx.send(f"`{station_name}` wird abgefragt, einen Moment bitte ...")

    try:
        locations = hafas.locations(station_name)
        if not locations:
            await ctx.send("Station nicht gefunden. Bitte überprüfe die Schreibweise.")
            return

        station = locations[0]

        departures = hafas.departures(
            station=station,
            date=datetime.datetime.now(),
            max_trips=5,
        )

        if not departures:
            await ctx.send("Keine bevorstehenden Abfahrten gefunden.")
            return

        message = f"**{station.name}** – Nächste Abfahrten:\n\n"
        for dep in departures:
            time_str = dep.dateTime.strftime("%H:%M")
            line = dep.name
            direction = dep.direction
            delay_str = ""

            if dep.delay and dep.delay.total_seconds() > 0:
                delay_min = int(dep.delay.total_seconds() / 60)
                delay_str = f" (+{delay_min} Min Verspätung)"

            message += f"- **{time_str}** | {line} -> {direction}{delay_str}\n"

        await ctx.send(message)

    except Exception as e:
        await ctx.send(f"Beim Abrufen der Daten ist ein Fehler aufgetreten: {e}")


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError(
            "Kein Discord-Token gefunden. Bitte lege eine .env-Datei mit "
            "DISCORD_TOKEN=dein_token an."
        )
    bot.run(TOKEN)
