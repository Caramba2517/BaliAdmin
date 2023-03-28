from aiogram.types import ParseMode
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from appart.models import Feedback
from aiogram import types, Bot, Dispatcher
import psycopg2

db = psycopg2.connect(
    host="85.92.111.75",
    database="default_db",
    user="gen_user",
    password="Golova123"
)

cur = db.cursor()


def get_tg_id(user_id):
    cur.execute("SELECT tg_id FROM appart_rentuser WHERE id=%s", (user_id,))
    result = cur.fetchone()
    return result


def keyboard() -> types.InlineKeyboardMarkup:
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('Close chat', callback_data='close_chat'),
         types.InlineKeyboardButton('Continue', callback_data='continue_chat')]
    ])

    return kb


@receiver(post_save, sender=Feedback)
def send_answer(sender, instance, **kwargs):
    async def send_message():
        bot = Bot(token='5993057930:AAEjmbPahvCocxdHu5w0K5HISwEOIX8PRuI')
        user_id = instance.user_id
        tg_id = get_tg_id(user_id)
        await bot.send_message(chat_id=tg_id[0],
                               text=f'<em>The administrator answered your question: {instance.text}\n\n</em>'
                                    f'<b>Answer:</b> {instance.answer}',
                               reply_markup=keyboard(),
                               parse_mode=ParseMode.HTML,
                               disable_notification=True,
                               disable_web_page_preview=True)

    async_to_sync(send_message)()
