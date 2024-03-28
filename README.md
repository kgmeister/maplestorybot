# Description: 
Bumblebee Bot is a custom bot for the 2D MMORPG game - MapleStory.  
This bot do not trigger in-game lie detector. 
It is open sourced and free to use. 

# Features:
- a

# Bot Limitations:
- Polo portal / Especia portal currently doesn't work on DMT day as the banner is blocking the top timer used to differentiate portal type. Users are suggested to turn portal feature off in settings tab. 
- When launcing on multiple PCs, cannot use the same telegram bot, must create a new tg bot for each PC. 

# Guide:
- this project uses python 3.12
- you can edit the code and run in cmd (administrator) using: python main.py
- run the following command to compile code into .exe file, then rename main.exe in dist folder to chrome.exe:
    - pyinstaller --clean --onefile --add-binary "./gdi_capture/gdi_capture.dll;." --icon=icon.ico main.py
- run the following command to disable console output:
    - pyinstaller --clean --noconsole --onefile --add-binary "./gdi_capture/gdi_capture.dll;." --icon=icon.ico main.py

# Discord Link: 
https://discord.gg/dbsKm2jE27

# Disclaimer:
We do not encourage botting. This project is only for research purpose. 

# Credits:
Part of the code taken from:
- https://github.com/qlvbrknp/maple-bot
