import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# BOT TOKEN
TOKEN = os.environ["8991385653:AAE9Vcwa9e_8XOGwEAGN76SscXPRYjcaGqM"]

# FOOTER
FOOTER = (
    "\n\n━━━━━━━━━━━━━━━━━━━━\n"
    "🙏 <b>Thanks for using Femzy Bot!</b>\n"
    "📞 <b>Phone:</b> +2349070528147\n"
    "📲 <b>Telegram:</b> @Femzynoir\n"
    "🎵 <b>TikTok:</b> @femzy4mena\n"
    "🔗 https://www.tiktok.com/@femzy4mena"
)

# MAIN MENU BUTTONS
MAIN_MENU = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🍎 iPhone", callback_data="cmd_iphone"),
        InlineKeyboardButton("🤖 Android", callback_data="cmd_android"),
    ],
    [
        InlineKeyboardButton("⚡ DPI", callback_data="cmd_dpi"),
        InlineKeyboardButton("🎮 HUD", callback_data="cmd_hud"),
    ],
    [
        InlineKeyboardButton("🔥 2 Finger HUD", callback_data="cmd_twofinger"),
        InlineKeyboardButton("⚡ 3 Finger HUD", callback_data="cmd_threefinger"),
    ],
    [
        InlineKeyboardButton("💀 4 Finger HUD", callback_data="cmd_fourfinger"),
        InlineKeyboardButton("🎯 Headshot Tips", callback_data="cmd_headshot"),
    ],
    [
        InlineKeyboardButton("📋 All Devices", callback_data="cmd_devices"),
        InlineKeyboardButton("🏆 Pro Tips", callback_data="cmd_tips"),
    ],
    [
        InlineKeyboardButton("🔫 Best Weapons", callback_data="cmd_weapons"),
        InlineKeyboardButton("🦸 Characters Combo", callback_data="cmd_characters"),
    ],
    [
        InlineKeyboardButton("🤝 Free Fire Collab", callback_data="cmd_collab"),
    ],
])

async def twofinger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("2f.jpg.JPG", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=(
                "🔥 <b>2 FINGER HUD</b> 🔥\n\n"
                "Best for easy drag headshots."
                + FOOTER
            ),
            parse_mode="HTML",
            reply_markup=BACK_BUTTON
        )

async def threefinger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("3f.jpg.JPG", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=(
                "⚡ <b>3 FINGER HUD</b> ⚡\n\n"
                "Balanced movement and aim."
                + FOOTER
            ),
            parse_mode="HTML",
            reply_markup=BACK_BUTTON
        )

async def fourfinger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("4f.jpg.JPG", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=(
                "💀 <b>4 FINGER PRO HUD</b> 💀\n\n"
                "Best for pro players and fast gameplay."
                + FOOTER
            ),
            parse_mode="HTML",
            reply_markup=BACK_BUTTON
        )
        file_map = {
    "cmd_twofinger": ("2f.jpg.JPG", "🔥 <b>2 FINGER HUD</b> 🔥\n\nBest for easy drag headshots."),
    "cmd_threefinger": ("3f.jpg.JPG", "⚡ <b>3 FINGER HUD</b> ⚡\n\nBalanced movement and aim."),
    "cmd_fourfinger": ("4f.jpg.JPG", "💀 <b>4 FINGER PRO HUD</b> 💀\n\nBest for pro players and fast gameplay."),
}
        
        
# BACK BUTTON
BACK_BUTTON = InlineKeyboardMarkup([
    [InlineKeyboardButton("🏠 Main Menu", callback_data="cmd_start")]
])
