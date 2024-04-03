# Description: 
Bumblebee Bot is a custom bot for the 2D MMORPG game - MapleStory.  
This bot does not trigger in-game lie detector in MapleSEA (tested), however not tested in other region MS / private server. 
It is open sourced and free to use. 

# Features:
- now possible to self-code high efficiency custom rotation. video showcase available in discord. 
- to_be_update

# Bot Limitations:
- Polo portal / Especia portal currently doesn't work on DMT day as the banner is blocking the top timer used to differentiate portal type. Users are suggested to turn portal feature off in settings tab. 
- When launcing on multiple PCs, cannot use the same telegram bot, must create a new tg bot for each PC. 

# Guide:
- this project uses python 3.12
- you can edit the code and run in cmd (administrator) using: python main.py
- join the discord server if you encounter any issue. (will update this section after stable. ) 
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
- https://github.com/kennyhml/pyinterception
