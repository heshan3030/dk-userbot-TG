import asyncio
import os

from telethon import __version__ 
from userbot import ALIVE_NAME, TG_CHANNEL, TG_GRUP
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd

LIGHTNING_ALV_IMG = os.environ.get("LIGHTNING_ALV_IMG", None)
if not LIGHTNING_ALV_IMG:
    LIGHTNING_ALV_IMG = "https://te.legra.ph/file/11664f82b88a5e16e6f26.mp4"


version = "4.5"
python_version = "3.8.5"

# Functions
def lightning_Read_time(seconds: int) -> str:
    count = 0
    kirsh = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            lol_hehehe, result = divmod(seconds, 60)
        else:
            lol_hehehe, result = divmod(seconds, 24)
        if seconds == 0 and lol_hehehe == 0:
            break
        time_list.append(int(result))
        seconds = int(lol_hehehe)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        kirsh += time_list.pop() + ", "

    time_list.reverse()
    kirsh += ":".join(time_list)

    return kirsh

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "โจ๐๐-๐๐๐๐-๐๐๐๐-๐๐๐โจ"

TG = str(TG_GRUP) if TG_GRUP else "Not  Yet๐๐"
TG_CHANN = str(TG_CHANNEL) if TG_CHANNEL else "Not Yet๐๐"


from userbot import CMD_LIST

pm_caption = "**โจ๐๐-๐๐๐๐-๐๐๐๐-๐๐๐โจ ๐เทเถเทโเถปเทเถบเท เถดเทเถญเท๐**\n\n"
pm_caption += f"**โเถธเถเท เถเถบเทเถญเทเถเถปเท** : {DEFAULTUSER}\n"
pm_caption += "**โเถธเถเท เทเถบเท**     : 1.17.5\n"
pm_caption += "**โเถธเถเท เถฏเทเถปเถเถฎเถฑ เถเถเถเถบ**  :[MY NUMBER](https://wa.me/message/0768100942)\n"
pm_caption += "**โเถฏเทเท เทเถปเทเถญเท เทเถธเทเทเถบ**   : [SUPPORT BOT](https://t.me/Datamaruwoteambot)\n"

pm_caption += "[๐ธ๊ฅ๏ฝ๊ฅ๐ธ ๐๐-๐๐๐๐-๐๐๐๐-๐๐๐ ๐ธ๊ฅ๏ฝ๊ฅ๐ธ](https://t.me/Datamaruwoteambot)"

@borg.on(lightning_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def lightning(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, file=LIGHTNING_ALV_IMG, caption=pm_caption, link_preview=False)
    await alive.delete()
