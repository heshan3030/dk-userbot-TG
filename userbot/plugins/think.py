"""Emoji

Available Commands:

.think"""

import asyncio

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd("think"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 288)

    # await event.edit(input_str)
    await event.edit("thinking")
    animation_chars = [
        "මතකයන්",
        "හිත පාරවයි",
        "වසන්තේ කොහොදෝ",
        "ගිහින්",
        "ජිවිතේ තැනක නැවතිලා",
        "මැකි යයි පිය සටහන්",
        "පාසලෙන්👩‍👩‍👦👩‍👩‍👦😪",
        "දුකයි",
        "තමයි",
        "මොනවා",
        "කරන්නද*",
        "ඉතිම්",
        "ඔහොම",
        "තමා ජිව්තේ",
        "හැටි😑....",
        "අනේ මන්දා😑😪... 🤔",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 72])
