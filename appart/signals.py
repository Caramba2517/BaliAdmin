from django.db.models.signals import post_save
from django.dispatch import receiver
from appart.models import Feedback
from asgiref.sync import async_to_sync
from aiogram import types, Bot, Dispatcher


@receiver(post_save, sender=Feedback)
def send_notification_on_approve(sender, instance, **kwargs):
    async def send_async_message():
        print(instance.user_id.tg_id)
        if instance.answer:
            bot = Bot(token='5993057930:AAEjmbPahvCocxdHu5w0K5HISwEOIX8PRuI')
            await bot.send_message(chat_id=instance.user_id.tg_id,
                                   text=f'{instance.answer}',
                                   disable_notification=True,
                                   disable_web_page_preview=True)

    return async_to_sync(send_async_message)()
