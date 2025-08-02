from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import MUSIC_BOT_NAME
from Oneforall import app


@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://files.catbox.moe/ix1sik.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ {MUSIC_BOT_NAME}\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🤍...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Gx-Toxic", url=f"https://t.me/Destiny_Infinity_Og"
                    ),
                    InlineKeyboardButton(
                        text="☆ ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/+2_dBLx7xZPk3YTI9"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="☆ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/dark_x_knight_musiczz_support"
                    ),
                ],
                [InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data="close")],
            ]
        ),
    )
