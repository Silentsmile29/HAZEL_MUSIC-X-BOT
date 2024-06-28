from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from HAZELMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ 𝑊𝑒𝑙𝑐𝑜𝑚𝑒 𝑇𝑜 𝐻𝑎𝑧𝑒𝑙 𝑀𝑢𝑠𝑖𝑐 𝑅𝑒𝑝𝑜 ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/+7K0IMwbLvAQwYmY1"),
             InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Silent_Smile_04"),
             ],
     
             [
             InlineKeyboardButton("𝗟𝗜𝗩𝗘 𝗖𝗖", url="https://t.me/+7K0IMwbLvAQwYmY1"),
             ],
     
             [
             InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://t.me/+7K0IMwbLvAQwYmY1"),            
             InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://github.com/Silentsmile29/HAZEL_MUSIC-X-BOT"),
             ],
     
             [
             InlineKeyboardButton("𝐄𝐕𝐈𝐋", url=f"https://t.me/+7K0IMwbLvAQwYmY1"),
             InlineKeyboardButton("𝐁𝐀𝐍 𝐀𝐋𝐋", url=f"https://t.me/+7K0IMwbLvAQwYmY1"),
             ],
     
             [
             InlineKeyboardButton("𝐀𝐋𝐋 𝐁𝐎𝐓𝐒", url=f"https://t.me/+7K0IMwbLvAQwYmY1"),
             InlineKeyboardButton("𝐁𝐎𝐓𝐕𝐄𝐑𝐒𝐄", url=f"https://t.me/+7K0IMwbLvAQwYmY1"),
             ],
     
              [
              InlineKeyboardButton("𝐆𝐈𝐓𝐇𝐔𝐁 𝐏𝐑𝐎𝐅𝐈𝐋𝐄", url=f"https://github.com/Silentsmile29"),
              InlineKeyboardButton("𝐕𝐈𝐂𝐊𝐘 𝐂𝐇𝐎𝐔𝐃𝐇𝐀𝐑𝐘 ♡︎", url=f"https://t.me/Silent_Smile_04"),
              ],
     
              [
              InlineKeyboardButton("𝐏𝐘𝐑𝐎𝐍𝐄", url=f"https://t.me/+7K0IMwbLvAQwYmY1"),
              InlineKeyboardButton("𝗔𝗟 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧", url=f"https://t.me/+7K0IMwbLvAQwYmY1"),
              ]
       ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/3ed81ef4e352a691fb0b4.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
