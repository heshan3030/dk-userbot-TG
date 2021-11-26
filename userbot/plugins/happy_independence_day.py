#plugin by @Dk_king_offcial

import asyncio
import random
from userbot import ALIVE_NAME
from userbot.utils import lightning_cmd
#Constant
yo = "https://te.legra.ph/file/6b2477183e62dbd2bda47.mp4"
yo2 = "https://te.legra.ph/file/363dec1f9f2af8ebb229a.jpg"
yo3 = "https://te.legra.ph/file/363dec1f9f2af8ebb229a.jpg"
#SED I HAVE NO MORE IF U HAVE I WILL UPDATE IT :)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "✨❝𝐃𝐊-𝐊𝐈𝐍𝐆-𝐔𝐒𝐄𝐑-𝐁𝐎𝐓❞✨"
remd = bot.me.id
cap =f"YEAH BRO 𝙷𝙰𝙿𝙿𝚈 𝙸𝙽𝙳𝙴𝙿𝙴𝙽𝙳𝙴𝙽𝙲𝙴 𝙳𝙰𝚈🇱🇰 TO [{DEFAULTUSER}](tg://user?id={remd})\n DONT FORGET TO CLICK 👉[dis](http://wish-style.com/?n=Rishisuperyo)👈\n ~ @Rishisuperyo"
#bruh

@borg.on(lightning_cmd(pattern=r"hpind", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("STARTING CELEBRATION OF 𝙷𝙰𝙿𝙿𝚈 𝙸𝙽𝙳𝙴𝙿𝙴𝙽𝙳𝙴𝙽𝙲𝙴 𝙳𝙰𝚈🇱🇰")
    await asyncio.sleep(3)
    s = random.randrange(1, 3)
    if s == 1:
    await event.edit("THANKS TO OUR SOLDIERS WHO ARE PROTECTING US IN BORDER , srilanka🇱🇰
  ගොන්ගාලේ ගොඩබණ්ඩා.වීර පුරන් අප්පු වැනි ශ්‍රේෂ්ඨ විරුවන් නිදහස ලබා ගැනීමේ සටනට නොබියව සටන් කළ අය වේ.වර්ෂ 1948 පෙබරවාරි මස 4 වැනිදා අපි ජාති භේද නොසලකා මහා සංග්‍රාමයකින් නිදහස ලැබුවෙමු.එය නිදහස් දිනයයි.

   නිදහස ලබා සිහලුන් සහ ජනයන්ගේ

   සිත් සතුටින් පිරුණි අසරණ මිනිසුන්ගේ

   අභිමානයට ලක්විය යුතු කරුණක් වේ")
    if s == 2:
        await event.edit(
        	     "BEFORE 73 YEARS WE GOT FREEDOM BY OUR FREEDOM FIGHTER, srilanka🇱🇰"
        )
    if s == 3:
        await event.edit(
        	     "WE SHOULD TAKE CARE OF OUR COUNTRY AND THANKS TO OUR SOLDIERS, Jsrilanka🇱🇰"
        )
    await bot.send_message(event.chat_id, "Please don't blink ur eyes a surprise iz coming")
    await asyncio.sleep(4)            
    f = random.randrange(1,3)
#try
    if f == 1:
       await bot.send_file(
        event.chat_id, file=yo ,caption=cap, link_preview=False
        )   
    if f == 2:
       await bot.send_file(
        event.chat_id, file=yo2 ,caption=cap, link_preview=False
       )
    if f == 3:
       await bot.send_file(
        event.chat_id, file=yo3 ,caption=cap, link_preview=False
       )
