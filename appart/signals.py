from aiogram.types import ParseMode
from asgiref.sync import async_to_sync, sync_to_async
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from appart.models import Feedback, SendMessageForAll, SendMessageForChooseUser, RentUser
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


def get_all_tg_id():
    cur.execute("SELECT tg_id FROM appart_rentuser")
    result = cur.fetchall()
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
        bot = Bot(token='6023288432:AAHwp3ZIci7gss9R1nI7-Iem5LFGsOWnKno')
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


def get_image(images):
    image_link = []
    for image in images:
        cur.execute("SELECT image FROM appart_image WHERE id=%s", (image,))
        image_link.append(cur.fetchone()[0]),
    return image_link


@receiver(post_save, sender=SendMessageForAll)
def send_message_for_all(sender, instance, **kwargs):
    async def send_message():
        bot = Bot(token='6023288432:AAHwp3ZIci7gss9R1nI7-Iem5LFGsOWnKno')
        all_id = get_all_tg_id()
        if instance.images:
            for tg_id in all_id:
                await bot.send_photo(chat_id=tg_id[0],
                                     photo=open(f'{instance.images}', 'rb'),
                                     caption=instance.text)
        else:
            for tg_id in all_id:
                await bot.send_message(chat_id=tg_id[0],
                                       text=instance.text)

    async_to_sync(send_message)()


@receiver(post_save, sender=SendMessageForChooseUser)
def send_message_for_choose(sender, instance, **kwargs):
    async def send_message():
        bot = Bot(token='6023288432:AAHwp3ZIci7gss9R1nI7-Iem5LFGsOWnKno')
        users = instance.users_id
        tg_id = get_tg_id(users)[0]
        if instance.images:
            await bot.send_photo(chat_id=tg_id,
                                 photo=open(f'{instance.images}', 'rb'),
                                 caption=instance.text)
        else:
            await bot.send_message(chat_id=tg_id,
                                   text=instance.text)

    async_to_sync(send_message)()
