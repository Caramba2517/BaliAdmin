import datetime
import psycopg2
import gspread
from oauth2client.service_account import ServiceAccountCredentials

db = psycopg2.connect(
    host="85.92.111.75",
    database="default_db",
    user="gen_user",
    password="Golova123"
)
cur = db.cursor()


def usd_statistic_query():
    now = datetime.datetime.now().date()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 0 AND 649")
    first = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 650 AND 1299")
    second = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 1300 AND 1949")
    third = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 1950 AND 2599")
    fourth = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 2600 AND 3249")
    fifth = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 3250 AND 1000000")
    sixth = cur.fetchone()
    cur.execute(f'INSERT INTO statistic_priceusdstatistic (date, first, second, third, fourth, fifth, sixth) '
                f'VALUES (%s, %s, %s, %s, %s, %s, %s)', (now, first, second, third, fourth, fifth, sixth,))
    db.commit()


def rup_statistic_query():
    now = datetime.datetime.now().date()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 0 AND 9999999")
    first = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 10000000 AND 19999999")
    second = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 20000000 AND 29999999")
    third = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 30000000 AND 39999999")
    fourth = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 40000000 AND 49999999")
    fifth = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 50000000 AND 1000000000")
    sixth = cur.fetchone()
    cur.execute(f'INSERT INTO statistic_pricerupstatistic (date, first, second, third, fourth, fifth, sixth) '
                f'VALUES (%s, %s, %s, %s, %s, %s, %s)', (now, first, second, third, fourth, fifth, sixth,))
    db.commit()


def location_statistic_query():
    now = datetime.datetime.now().date()
    cur.execute("SELECT DISTINCT location_id FROM appart_apartment")
    locations = cur.fetchall()
    text = ''
    for location in locations:
        cur.execute(f"SELECT COUNT(*) from appart_apartment WHERE location_id = {location[0]}")
        result = cur.fetchone()
        cur.execute(f"SELECT name from appart_location WHERE id = {location[0]}")
        location_name = cur.fetchone()
        text += f'{location_name[0]} - {result[0]}\n'
    cur.execute("INSERT INTO statistic_locationstatistic (date, index) VALUES (%s, %s)", (now, text,))
    db.commit()


def ads_statistic_query():
    now = datetime.datetime.now().date()
    cur.execute("SELECT COUNT (*) from appart_apartment")
    total_result = cur.fetchone()
    db.rollback()
    cur.execute(f"SELECT COUNT (*) from appart_apartment WHERE date = '{now}'")
    daily_result = cur.fetchone()
    db.rollback()
    if daily_result is None:
        daily_result = 0
    cur.execute(f"INSERT INTO statistic_adsstatistic (date, total, daily) VALUES (%s, %s, %s)",
                (now, total_result[0], daily_result[0],))
    db.commit()


class Scheduler(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'statistic_scheduler'

    @staticmethod
    def do():
        usd_statistic_query()
        rup_statistic_query()
        location_statistic_query()
        ads_statistic_query()
