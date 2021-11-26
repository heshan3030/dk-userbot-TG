"""Emoji

Available Commands:

.wtf"""


import asyncio

from userbot.utils import DK-KING-USER-BOT_cmd


@borg.on(lightning_cmd("wtf"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("wtf")
    animation_chars = [
        "What",
        "What The F",
        "What The Fu",
        "What The Fuck",
        "[What The Fuck](https://te.legra.ph/file/b862626b4df2e6ed2af1d.jpg)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])
