# Description: 
Bumblebee Bot is a custom bot for the 2D MMORPG game - MapleStory.  
This bot does not trigger in-game lie detector in MapleSEA (tested), however not tested in other region MS / private server. 
It is open sourced and free to use. 

Bumblebee Bot 是专为2D MMORPG 游戏《楓之谷》定制的外挂。
该外挂在《楓之谷》东南亚服务器(经过测试）（MapleStorySEA）中不会触发游戏内的测谎仪，但在其他地区的《楓之谷》或私人服务器上未经测试。
该外挂是开源的，并且免费使用。

Bumblebee Bot은 2D MMORPG 게임 '메이플스토리'를 위해 맞춤으로 개발된 외부 도구입니다. 이 도구는 '메이플스토리' 동남아 서버(MapleStorySEA)에서 내장된 거짓탐지기를 작동시키지 않습니다(테스트 완료). 그러나 다른 지역의 '메이플스토리'나 사설 서버에서는 테스트되지 않았습니다. 이 도구는 오픈 소스이며 무료로 사용할 수 있습니다.

# Features:
- now possible to self-code high efficiency custom rotation. video showcase available in discord. 
- GMA detector. (need external chat window)
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
