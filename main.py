import asyncio
import instaloader
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import CommandStart

bot = Bot(token='BOT_FATHER_BERGAN_API_TOKEN')
dp = Dispatcher()

new_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='♻️Yangilash', callback_data='new')]
])

username = ''

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer('❌@username 👉 ✅username')

@dp.message(F.text)
async def get(message: Message):
    global username
    username = message.text
    L=instaloader.Instaloader()
    profile=instaloader.Profile.from_username(L.context,username)
    await message.answer(f'✅@{username}\n\n👥Obunachilar: {profile.followers}\n🫂Obunalar: {profile.followees}\n🗣Postlar: {profile.mediacount}',reply_markup=new_btn)

@dp.callback_query(F.data)
async def new(callback: CallbackQuery):
    global username
    L=instaloader.Instaloader()
    profile=instaloader.Profile.from_username(L.context,username)
    await callback.answer('✅Yangilandi')
    await callback.message.edit_text(f'✅@{username}\n\n👥Obunachilar: {profile.followers}\n🫂Obunalar: {profile.followees}\n🗣Postlar: {profile.mediacount}',reply_markup=new_btn)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
