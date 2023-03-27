from loader import dp
from aiogram.types import Message
from aiogram.dispatcher import filters
from Keyboards.Standart.dynamic import create_kb


@dp.message_handler(filters.Text('текст'))
async def help_command(message: Message):
    await message.answer(f'Ты смотри текст написан',
                         reply_markup=create_kb(message))