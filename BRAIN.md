# Brain — Development Notes

This file isn't for end users — it's to guide ongoing development (me and Claude). User-facing docs live in README.md.

## Current state

- Single file: [bot.py](bot.py) — discord.py + pyhafas (VSNProfile).
- Token is read from `DISCORD_TOKEN` in `.env` (via `python-dotenv`), not hardcoded.
- All user-facing messages and code comments are in German — target audience is Discord users in the VSN region. Keep this language; don't mix in Turkish/English.
- Commands: `!test`, `!tren <station name>`.
- No `requirements.txt` yet; the README references it but the file isn't in the repo.

## Known gaps

- Missing `requirements.txt` (discord.py, pyhafas, python-dotenv).
- Everything lives in one file; should be split into modules if it grows (new commands, other APIs).
- Error handling is a single generic `except Exception` — no API-specific error types.
- No tests.

## Decisions / why

- Using VSNProfile instead of the DB (Deutsche Bahn) HAFAS profile because the DB server was down/unstable.
- Secrets live in `.env`, not committed (`.env` added to `.gitignore`).

## Next steps (not done yet, just ideas)

- Add `requirements.txt`.
