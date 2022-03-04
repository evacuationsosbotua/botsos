from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




#main menu 
btnMain = KeyboardButton('📝 Подати заяву на евакуацію') 
btnSupport = KeyboardButton('💬 Жива підтримка')
btnContact = KeyboardButton('Контакти')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnMain, btnSupport, btnContact)
