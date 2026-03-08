# Discord Transit Bot (pyhafas)

Ein asynchroner Discord-Bot, der Echtzeit-Verbindungen, Abfahrtszeiten und Verspätungen im öffentlichen Nahverkehr direkt in einen Discord-Server integriert. 

## 🛠 Technologien & Tools
* **Programmiersprache:** Python 3
* **Bibliotheken:** `discord.py` (für die asynchrone Discord-API Kommunikation), `pyhafas` (für den Zugriff auf die Hafas-basierten Fahrplandaten)
* **API:** VSN Profile (als stabile Alternative für das DB-Backend) zur Abfrage der Echtzeitdaten.

##  Features
* **Echtzeit-Abfragen:** Durch den Befehl `!tren [Bahnhofsname]` sucht der Bot den entsprechenden Bahnhof in der API.
* **Verspätungsanzeige:** Die nächsten 5 Abfahrten werden live abgerufen. Etwaige Verspätungen werden automatisch berechnet und farblich (🔴) markiert dargestellt.
* **Fehlerbehandlung:** Integrierte Exception-Handlings für API-Ausfälle, Namensauflösungsfehler (NameResolutionError) oder falsche Usereingaben.

## Motivation & Lerneffekt
Dieses Projekt wurde entwickelt, um praktische Erfahrungen im Umgang mit externen APIs, asynchroner Programmierung in Python sowie dem Handling von JSON-ähnlichen Datenstrukturen zu sammeln. Zudem wurde Fokus auf robuste Problemlösung gelegt (z.B. Wechsel des API-Profils bei Ausfall der primären DB-Schnittstelle).
