"""Restart or Terminate the bot from any chat
Available Commands:
.restartsys
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
import asyncio
import os
import sys

from uniborg.util import DK-KING-USER-BOT_cmd


@borg.on(DK-KING-USER-BOT_cmd(pattern="restart"))
async def _(event):
    await event.edit(
        "DK-KING-USER-BOT ‼️♻️අපගේ සහකාරුගේ පද්ධතියේ දෝෂයකි♻️‼️...🔄restart කිරීම සාර්ථකව සිදු කර ඇත.🔄...මේ සදහා විනාඩි 2-3 කාලයක් ගතවනු ඇත.මදක් රැදි සිටින්න😇"
    )
    await borg.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@borg.on(DK-KING-USER-BOT_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning dynos off... Whenever you want to start me open dynos manually.")
    await borg.disconnect()
