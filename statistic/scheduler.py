from aiogram import Dispatcher, types, Bot
import asyncio
import datetime
import psycopg2

db = psycopg2.connect(
    host="92.53.127.97",
    database="default_db",
    user="gen_user",
    password="Tim262Tim262"

)

cur = db.cursor()


def get_records():
    cur.execute(
        "SELECT client FROM rent WHERE EXTRACT(EPOCH FROM (CAST(date_finish AS TIMESTAMP) - "
        "CAST(date_start AS TIMESTAMP))) > 604800 AND date_finish = CURRENT_DATE + INTERVAL '3 days'")
    results = cur.fetchall()
    if results:
        tg_id = []
        for result in results:
            cur.execute("SELECT tg_id FROM client WHERE id=%s", (result,))
            tg_id += cur.fetchone()
        return tg_id
    else:
        pass


def get_records_more_30_days():
    cur.execute(
        "SELECT client FROM rent WHERE EXTRACT(EPOCH FROM (CAST(CURRENT_DATE AS TIMESTAMP) - "
        "CAST(date_start AS TIMESTAMP))) = 2160000 AND EXTRACT(EPOCH FROM (CAST(date_finish AS TIMESTAMP) - "
        "CAST(date_start AS TIMESTAMP))) >= 2592000")
    results = cur.fetchall()
    if results:
        tg_id = []
        for result in results:
            cur.execute("SELECT tg_id FROM client WHERE id=%s", (result,))
            tg_id += cur.fetchone()
        print(tg_id)

        return tg_id
    else:
        pass



async def send_message_daily(tg_id, msg, x):
    bot = Bot.get_current()
    if bot is None:
        bot = Bot(token=keys.token)
        Bot.set_current(bot)
    if tg_id:
        for tg in tg_id:
            print(tg)
            await bot.send_message(chat_id=tg,
                                   text=msg,
                                   reply_markup=x)


async def run_daily_task():
    print(f"Scheduler run at {datetime.datetime.now()}")
    while True:
        now = datetime.datetime.now()
        if now.hour == 10 and now.minute == 00:
            tg_id = get_records_more_30_days()
            msg = f"Dear client, please input your current bike mileage.\n" \
                  f"We keep all our bikes in best condition and need to dо service in time"
            x = keyboard.inline.kb_mileage_client()
            await send_message_daily(tg_id, msg, x)
            print(f"get_records_more_30_days completed at {datetime.datetime.now()}")
        if now.hour == 10 and now.minute == 30:
            tg_id = get_records()
            msg = f'Kindly inform you that your rent will finish in 3 days.\n\nWould you like to extend your rent?'
            x = keyboard.inline.kb_yesno()
            await send_message_daily(tg_id, msg, x)
            print(f"get_records completed at {datetime.datetime.now()}")
        await asyncio.sleep(60 - now.second)


if __name__ == '__main__':
    asyncio.run(run_daily_task())