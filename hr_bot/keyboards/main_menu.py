from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🏢 О компании")],
        [KeyboardButton(text="📚 Начать обучение")],
        [KeyboardButton(text="❓ FAQ")],
        [KeyboardButton(text="📞 Контакты")]
    ],
    resize_keyboard=True
)

print("MAIN MENU LOADED")