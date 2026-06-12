# Discord Transit Bot (ÖPNV)

Ein asynchroner Discord-Bot, der Echtzeit-Verbindungen, Abfahrtszeiten und Verspätungen im öffentlichen Nahverkehr (ÖPNV) direkt in einen Discord-Server integriert.

## Funktionen

- **Echtzeit-Abfragen:** Mit dem Befehl `!tren [Bahnhofsname]` sucht der Bot den passenden Bahnhof über die API und ruft die aktuellen Verbindungen ab.
- **Verspätungsanzeige:** Die nächsten fünf Abfahrten werden live abgerufen; Verspätungen werden automatisch berechnet und hervorgehoben.
- **Fehlerbehandlung:** Integriertes Exception-Handling für API-Ausfälle, Namensauflösungsfehler (NameResolutionError) und fehlerhafte Benutzereingaben.

## Technologien

- **Sprache:** Python 3
- **Bibliotheken:** `discord.py` (asynchrone Kommunikation mit der Discord-API), `pyhafas` (Zugriff auf HAFAS-basierte Fahrplandaten)
- **API:** VSN-Profil als stabile Alternative zum DB-Backend für die Echtzeitabfragen

## Installation & Einrichtung

**Voraussetzungen:** Python 3.x und ein Discord-Bot-Token (über das [Discord Developer Portal](https://discord.com/developers/applications)).

1. Repository klonen:
   ```bash
   git clone https://github.com/omerdolek88/discord-transit-bot.git
   cd discord-transit-bot
   ```

2. (Empfohlen) Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   # Falls keine requirements.txt vorhanden ist:
   # pip install discord.py pyhafas
   ```

4. Discord-Token hinterlegen – eine Datei `.env` im Projektordner anlegen:
   ```
   DISCORD_TOKEN=dein_token_hier
   ```

5. Bot starten:
   ```bash
   python bot.py
   ```

## Nutzung

1. Den Bot über das Developer Portal auf den gewünschten Discord-Server einladen.
2. Im Chat den Befehl eingeben:
   ```
   !tren Bonn Hbf
   ```
3. Der Bot zeigt die nächsten fünf Abfahrten inklusive etwaiger Verspätungen an.

## Motivation & Lerneffekt

Das Projekt wurde entwickelt, um praktische Erfahrung im Umgang mit externen APIs, asynchroner Programmierung in Python und der Verarbeitung von JSON-ähnlichen Datenstrukturen zu sammeln. Ein besonderer Fokus lag auf robuster Problemlösung – beispielsweise dem Wechsel des API-Profils beim Ausfall der primären Schnittstelle.
