"""COMMAND : ./cull"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "/cull":

        await event.edit(input_str)

        animation_chars = [
     
    "Calling Dialog 📞📞...",
            "...🙏ආයුබොවන් wellcome  To dialog🙏...",
            "✅සිංහල බසින් සේවාව දිගටම පවත්වා ගෙන යාම  සදහා අංක 1 ඇතුළත් කරන්න.",
            "✅වෙනත් භාෂාව තොර ගැනීමට අවශ්‍ය නම් අංක 2 ඇතුළත් කරන්න",
            "✅mobile සදහා අංක 1 ඇතුළත් කරන්න",
            "✅ezcash සදහා අංක  2 ඇතුලත් කරන්න.",
            "✅වෙනත්  ව්‍යාපාරික අංශයක් වෙත (යොමු විමට අවශ්‍ය නම් අංක 3 ඇතුළත් කරන්න",
            "✅ඔබගේ ගිණුමේ ඇති මුදල් ප්‍රමාණය දැන ගැනීමට අවශ්‍ය නම් අංක 1 ඇතුළත් කරන්න...",
            "✳️ඔබගේ ගිණුමේ දැන පවතින ශේෂය වන්නේ රුපියල් 0 වයි...",    
            "🔄ගිණුම රිචාර්ජ් කිරීම සදහා අංක 2 ඇතුළත් කරන්න ",
            "😄ණය මුදලක් ලබාගැනීමට අවශ්‍ය නම් අංක 3 ඇතුළත් කරන්න",
            "⬅️නැවත පෙර මෙනුම වෙත යාමට අවශ්‍ය නම් අංක 4 ඇතුළත් කරන්න..සේවාව දිගටම පවත්වා ගෙන යාම සදහා අංක 7 ඇතුළත් කරන්න.",
            "..........👩‍💼🧑‍💼පරිභෝගික සේවා නිලධාරීයකු සම්බන්ධ විමට අවශ්‍ය නම් අංක 8 ඇතුළත් කරන්න..",
            "🗣✅හිතවත් පරිභෝගිකය ඔබ මාසයක් ඇතුළත අප පරිභෝගික සේවා නිලධාරීයකු වෙත ලබාගන්නා 3 න් වෙනි ඇමතුමේ සිට ඔබට රුපියල් 3ක් රජයේ අදාළ බදු අය  කේරේ...",
            "✅සේවාව දිගටම පවත්වා ගෙන යාම සදහා අංක 1 ඇතුළත් කරන්න",
         "👩‍💼🧑‍💼අපගේ පරිභෝගික නිලධාරීන් කර්යය බහුල බැවින් මදක් රැදි සිටින්න..",
             ".🗣..හෙලෝ ආයුබොවන් සර්..ඔබගේ ගැටලුව කුමක්ද?.",
            "මිස් මගේ සල්ලියි. ඩේටායි ඉවරයිනේ🥺..මම කතා කරෙත් නැනේ.ආ ඔව් සර් එකටනේ කියන්නේ අනාගත අදයි කියලා..😂..ට හුකන්ඩ තියපන් හු##🤬 පොන් එක",
            "Private Call Disconnected😹."
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
