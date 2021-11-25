#!/bin/bash
clear
echo "
  _____  _  __     _  _______ _   _  _____        _    _  _____ ______ _____        ____   ____ _______ 
 |  __ \| |/ /    | |/ /_   _| \ | |/ ____|      | |  | |/ ____|  ____|  __ \      |  _ \ / __ \__   __|
 | |  | | ' /_____| ' /  | | |  \| | |  __ ______| |  | | (___ | |__  | |__) |_____| |_) | |  | | | |   
 | |  | |  <______|  <   | | | . ` | | |_ |______| |  | |\___ \|  __| |  _  /______|  _ <| |  | | | |   
 | |__| | . \     | . \ _| |_| |\  | |__| |      | |__| |____) | |____| | \ \      | |_) | |__| | | |   
 |_____/|_|\_\    |_|\_\_____|_| \_|\_____|       \____/|_____/|______|_|  \_\     |____/ \____/  |_|   
                                                                                                        
    "
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/Anmol-dot283/dk-userbot-TG/master/resources/lightning-setup.py
pip3 install telethon
python3 telebot-setup.py
