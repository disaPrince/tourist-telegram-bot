@echo

call %~dp0venv\Scripts\activate

cd %~dp0

set TOKEN=5134725968:AAG5yo4yrJQ9JgeBiCwsJJt3fanGEqKZBzU

python telegram_bot.py

pause