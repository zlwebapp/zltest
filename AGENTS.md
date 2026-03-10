# AGENTS.md

## Cursor Cloud specific instructions

This is a single-file Python CLI project (`collect_weather.py`) that fetches Shanghai weather data from the public Open-Meteo API and appends it to `shanghai_weather_daily.json`.

- **Run the app**: `python3 collect_weather.py`
- **Dependencies**: `pip install -r requirements.txt` (only `requests>=2.28`)
- **No API key required**: Open-Meteo is a free public API.
- The script writes `shanghai_weather_daily.json` in the repo root; this file is not committed and is generated at runtime.
- No lint, test, or build tooling is configured in this repo. There are no test suites, linters, or CI pipelines.
- Internet access is required to call `https://api.open-meteo.com/v1/forecast`.
