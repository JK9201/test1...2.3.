from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"""
╭────────────────乂─────────────────๏
╰๏**𝘋𝘌𝘝𝘐𝘓 𝘟 𝘏𝘌𝘓𝘗 𝘔𝘌𝘕𝘜 🍷💕**
╰๏
╰๏**𝘊𝘓𝘐𝘊𝘒 𝘖𝘕 𝘉𝘌𝘓𝘖𝘞 𝘉𝘜𝘛𝘛𝘖𝘕𝘚 𝘍𝘖𝘙 𝘏𝘌𝘓𝘗 🍁**
╰๏
╰๏**𝘋𝘌𝘝 💕: @KANU_XD 🍻**
╰────────────────乂─────────────────๏
"""
HELP_BUTTON = [
    [
      Button.inline("✦ 𝘚𝘗𝘈𝘔 ✦", data="spam"),
      Button.inline("✦ 𝘙𝘈𝘐𝘋 ✦", data="raid")
    ],
    [
      Button.inline("✦ 𝘌𝘟𝘛𝘙𝘈 ✦", data="extra")
    ],
    [
      Button.url("✦ 𝘎𝘙𝘖𝘜𝘗 ✦", "https://t.me/FriendCastel"),
      Button.url("✦ 𝘚𝘜𝘗𝘗𝘖𝘙𝘛 ✦", "https://t.me/UNI_INDIA_0008")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://graph.org/file/0fba871849965974d8ddb.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"𝘈𝘕 𝘌𝘟𝘊𝘌𝘗𝘛𝘐𝘖𝘕 𝘖𝘊𝘊𝘜𝘙𝘌𝘋 ! !\n\n**𝘌𝘙𝘙𝘖𝘙:** {str(e)}")


extra_msg = f"""
**» 
𝗨𝘀𝗲𝗿𝗕𝗼𝘁⦂ **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ**
  1️⃣) {​🇭​​🇱​}​🇵​​🇮​​🇳​​🇬​ 
  2️⃣) {​🇭​​🇱​}​🇷​​🇪​​🇧​​🇴​​🇴​​🇹​
  3️⃣) {​🇭​​🇱​}​🇸​​🇺​​🇩​​🇴​ <​🇷​​🇪​​🇵​​🇱​​🇾​ ​🇹​​🇴​ ​🇺​​🇸​​🇪​​🇷​>  --> ​🇴​​🇼​​🇳​​🇪​​🇷​ ​🇨​​🇲​​🇩​
  4️⃣) {​🇭​​🇱​}​🇱​​🇴​​🇬​​🇸​ --> ​🇴​​🇼​​🇳​​🇪​​🇷​ ​🇨​​🇲​​🇩​

𝗘𝗰𝗵𝗼⦂ **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**
  1️⃣) {​🇭​​🇱​}​🇪​​🇨​​🇭​​🇴​ <​🇷​​🇪​​🇵​​🇱​​🇾​ ​🇹​​🇴​ ​🇺​​🇸​​🇪​​🇷​>
  2️⃣) {​🇭​​🇱​}​🇷​​🇲​​🇪​​🇨​​🇭​​🇴​ <​🇷​​🇪​​🇵​​🇱​​🇾​ ​🇹​​🇴​ ​🇺​​🇸​​🇪​​🇷​>

𝗟𝗲𝗮𝘃𝗲⦂ **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**
  1️⃣) {​🇭​​🇱​}​🇱​​🇪​​🇦​​🇻​​🇪​ <​🇬​​🇷​​🇴​​🇺​​🇵​/​🇨​​🇭​​🇦​​🇹​ ​🇮​​🇩​>
  2️⃣) {​🇭​​🇱​}​🇱​​🇪​​🇦​​🇻​​🇪​ ⦂ ​🇹​​🇾​​🇵​​🇪​ ​🇮​​🇳​ ​🇹​​🇭​​🇪​ ​🇬​​🇷​​🇴​​🇺​​🇵​ ​🇧​​🇴​​🇹​ ​🇼​​🇮​​🇱​​🇱​ ​🇦​​🇺​​🇹​​🇴​ ​🇱​​🇪​​🇦​​🇻​​🇪​ ​🇹​​🇭​​🇦​​🇹​ ​🇬​​🇷​​🇴​​🇺​​🇵​

**@rasedidstore**
"""

                 
raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ⦂**

𝗥𝗮𝗶𝗱⦂ **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**
  1️⃣) {​🇭​​🇱​}​🇷​​🇦​​🇮​​🇩​ <​🇨​​🇴​​🇺​​🇳​​🇹​> <​🇺​​🇸​​🇪​​🇷​​🇳​​🇦​​🇲​​🇪​>
  2️⃣) {​🇭​​🇱​}​🇷​​🇦​​🇮​​🇩​ <​🇨​​🇴​​🇺​​🇳​​🇹​> <​🇷​​🇪​​🇵​​🇱​​🇾​ ​🇹​​🇴​ ​🇺​​🇸​​🇪​​🇷​>

𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱⦂ **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1️⃣) {​🇭​​🇱​}​🇷​​🇷​​🇦​​🇮​​🇩​ <​🇷​​🇪​​🇵​​🇱​​🇾​​🇮​​🇳​​🇬​ ​🇹​​🇴​ ​🇺​​🇸​​🇪​​🇷​>
  2️⃣) {​🇭​​🇱​}​🇷​​🇷​​🇦​​🇮​​🇩​ <​🇺​​🇸​​🇪​​🇷​​🇳​​🇦​​🇲​​🇪​>

𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱⦂ **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1️⃣) {​🇭​​🇱​}​🇩​​🇷​​🇷​​🇦​​🇮​​🇩​ <​🇷​​🇪​​🇵​​🇱​​🇾​​🇮​​🇳​​🇬​ ​🇹​​🇴​ ​🇺​​🇸​​🇪​​🇷​>
  2️⃣) {​🇭​​🇱​}​🇩​​🇷​​🇷​​🇦​​🇮​​🇩​ <​🇺​​🇸​​🇪​​🇷​​🇳​​🇦​​🇲​​🇪​>

𝐌𝐑𝐚𝐢𝐝⦂ **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1️⃣) {​🇭​​🇱​}​🇲​​🇷​​🇦​​🇮​​🇩​ <​🇨​​🇴​​🇺​​🇳​​🇹​> <​🇺​​🇸​​🇪​​🇷​​🇳​​🇦​​🇲​​🇪​>
  2️⃣) {​🇭​​🇱​}​🇲​​🇷​​🇦​​🇮​​🇩​ <​🇨​​🇴​​🇺​​🇳​​🇹​> <​🇷​​🇪​​🇵​​🇱​​🇾​ ​🇹​​🇴​ ​🇺​​🇸​​🇪​​🇷​>

𝐒𝐑𝐚𝐢𝐝⦂ **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1️⃣) {​🇭​​🇱​}​🇸​​🇷​​🇦​​🇮​​🇩​ <​🇨​​🇴​​🇺​​🇳​​🇹​> <​🇺​​🇸​​🇪​​🇷​​🇳​​🇦​​🇲​​🇪​>
  2️⃣) {​🇭​​🇱​}​🇸​​🇷​​🇦​​🇮​​🇩​ <​🇨​​🇴​​🇺​​🇳​​🇹​> <​🇷​​🇪​​🇵​​🇱​​🇾​ ​🇹​​🇴​ ​🇺​​🇸​​🇪​​🇷​>

𝐂𝐑𝐚𝐢𝐝⦂ **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1️⃣) {​🇭​​🇱​}​🇨​​🇷​​🇦​​🇮​​🇩​ <​🇨​​🇴​​🇺​​🇳​​🇹​> <​🇺​​🇸​​🇪​​🇷​​🇳​​🇦​​🇲​​🇪​>
  2️⃣) {​🇭​​🇱​}​🇨​​🇷​​🇦​​🇮​​🇩​ <​🇨​​🇴​​🇺​​🇳​​🇹​> <​🇷​​🇪​​🇵​​🇱​​🇾​ ​🇹​​🇴​ ​🇺​​🇸​​🇪​​🇷​>


**@rasedidstore**
"""

spam_msg = f"""
**» 𝓢𝓟𝓐𝓜 𝓒𝓞𝓜𝓜𝓐𝓝𝓓𝓢:**

𝓢𝓟𝓐𝓜: **𝓢𝓟𝓐𝓜𝓢 𝓐 𝓜𝓔𝓢𝓢𝓐𝓖𝓔**
  1) {hl}𝓢𝓟𝓐𝓜 <𝓬𝓸𝓾𝓷𝓽> <𝓶𝓮𝓼𝓼𝓪𝓰𝓮 𝓽𝓸 𝓼𝓹𝓪𝓶>
  2) {hl}𝓢𝓟𝓐𝓜 <𝓬𝓸𝓾𝓷𝓽> <𝓻𝓮𝓹𝓵𝔂𝓲𝓷𝓰 𝓪𝓷𝔂 𝓶𝓮𝓼𝓼𝓪𝓰𝓮>

𝓟𝓞𝓡𝓝𝓢𝓟𝓐𝓜: **𝓟𝓞𝓡𝓜𝓞𝓖𝓡𝓐𝓟𝓗𝓨 𝓢𝓟𝓐𝓜**
  1) {hl}𝓟𝓢𝓟𝓐𝓜 <𝓬𝓸𝓾𝓷𝓽>

𝓗𝓐𝓝𝓖: **𝓢𝓟𝓐𝓜𝓢 𝓗𝓐𝓝𝓖𝓘𝓝𝓖 𝓜𝓔𝓢𝓢𝓐𝓖𝓔 𝓕𝓞𝓡 𝓖𝓘𝓥𝓔𝓝 𝓒𝓞𝓤𝓝𝓣𝓔𝓡**
  1) {hl}𝓗𝓐𝓝𝓖 <𝓬𝓸𝓾𝓷𝓽>


**@rasedidstore**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("• 𝓢𝓟𝓐𝓜 •", data="spam"),
                Button.inline("• 𝓡𝓐𝓘𝓓 •", data="raid")
              ],
              [
                Button.inline("• 𝓔𝓧𝓣𝓡𝓐 •", data="extra")
              ],
              [
                Button.url("• 𝓖𝓡𝓞𝓤𝓟 •", "https://t.me/FriendCastel"),
                Button.url("• 𝓢𝓤𝓟𝓟𝓞𝓡𝓣 •", "https://t.me/UNI_INDIA_0008")
              ]
            ]
          )
    else:
        await event.answer("𝓜𝓐𝓚𝓔 𝓨𝓞𝓤𝓡 𝓞𝓦𝓝 𝓓𝓔𝓥𝓘𝓛 𝓧 𝓑𝓞𝓣𝓢 !! @rasedidstore", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< 𝓑𝓪𝓬𝓴", data="𝓱𝓮𝓵𝓹_𝓫𝓪𝓬𝓴"),],],
              ) 
    else:
        await event.answer("𝓜𝓐𝓚𝓔 𝓨𝓞𝓤𝓡 𝓞𝓦𝓝 𝓓𝓔𝓥𝓘𝓛 𝓧 𝓑𝓞𝓣𝓢 !! @rasedidstore", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< 𝓑𝓪𝓬𝓴", data="𝓱𝓮𝓵𝓹_𝓫𝓪𝓬𝓴"),],],
          )
    else:
        await event.answer("𝓜𝓐𝓚𝓔 𝓨𝓞𝓤𝓡 𝓞𝓦𝓝 𝓓𝓔𝓥𝓘𝓛 𝓧 𝓑𝓞𝓣𝓢 !! @rasedidstore", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< 𝓑𝓪𝓬𝓴", data="𝓱𝓮𝓵𝓹_𝓫𝓪𝓬𝓴"),],],
            )
    else:
        await event.answer("𝓜𝓐𝓚𝓔 𝓨𝓞𝓤𝓡 𝓞𝓦𝓝 𝓓𝓔𝓥𝓘𝓛 𝓧 𝓑𝓞𝓣𝓢 !! @rasedidstore", cache_time=0, alert=True)
