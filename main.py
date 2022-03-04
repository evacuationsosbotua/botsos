import logging 
from aiogram import Bot, Dispatcher, executor, types
# import markups as nav

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "5110637683:AAFxV4HSpgsfwBGeX-FtlzORA1o9DVi1KKE" 

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)



#buttons 

urlButtons = InlineKeyboardMarkup(row_width=1)
sendFormButton = InlineKeyboardButton(text='📝 Подати заяву на евакуацію 📝', url='https://forms.gle/EMBTYZ8KKhCA5hwo8')
liveChatButton = InlineKeyboardButton(text='💬 Жива підтримка 💬', url='https://t.me/evacuation_war')
urlButtons.add(sendFormButton, liveChatButton)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
	await message.answer_photo('https://1944718.artcoco.web.hosting-test.net/evacuation_post.png')
	await bot.send_message(message.from_user.id, 'Вітаємо!🇺🇦🇺🇦🇺🇦\n\nВи звернулися до офіційного чат-боту центру підтримки "Евакуація".\n\nЯкщо Ви або Ваш родич потребує негайної допомоги з переселення, заповніть форму зазначину нижче і ми неодмінно надамо допомогу!'.format(message.from_user), reply_markup = urlButtons)
	# await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler()
async def bot_message(message: types.Message):
	#await bot.send_message(message.from_user.id, message.text)
	if message.text != '/start':
		await bot.send_message(message.from_user.id, 'Вибачте! \n Але ми не змогли розібрати Ваш запит. \n Скористайетсь командою /start')


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)