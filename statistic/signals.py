import datetime
import psycopg2
import gspread
from oauth2client.service_account import ServiceAccountCredentials

db = psycopg2.connect(
    host="db-villabot-do-user-13857954-0.b.db.ondigitalocean.com",
    database="defaultdb",
    user="doadmin",
    password="AVNS_9TWJQ4KUZGhFG6d7kFX",
    port="25060"
)

cur = db.cursor()


def usd_statistic_query():
    now = datetime.datetime.now().date()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 300 AND 649")
    first = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 650 AND 1299")
    second = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 1300 AND 1949")
    third = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 1950 AND 2599")
    fourth = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 2600 AND 3249")
    fifth = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_usd BETWEEN 3250 AND 5000")
    sixth = cur.fetchone()

    # Count apartments in different price ranges per day
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 0 AND 19")
    first_day = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 20 AND 49")
    second_day = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 50 AND 69")
    third_day = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 70 AND 99")
    fourth_day = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 100 AND 139")
    fifth_day = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 139 AND 300")
    sixth_day = cur.fetchone()

    # Count apartments in different price ranges per year
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 5000 AND 7999")
    first_year = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 8000 AND 15999")
    second_year = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 16000 AND 23999")
    third_year = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 24000 AND 31999")
    fourth_year = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd BETWEEN 32000 AND 39999")
    fifth_year = cur.fetchone()
    cur.execute("SELECT COUNT(*) FROM appart_apartment WHERE price_usd >= 40000")
    sixth_year = cur.fetchone()
    cur.execute(
        f'INSERT INTO statistic_priceusdstatistic (date, first_month, second_month, third_month, fourth_month, fifth_month, sixth_month,'
        f'first_day, second_day, third_day, fourth_day, fifth_day, sixth_day,'
        f'first_year, second_year, third_year, fourth_year, fifth_year, sixth_year) '
        f'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (now, first, second, third, fourth, fifth, sixth,
         first_day, second_day, third_day, fourth_day, fifth_day, sixth_day,
         first_year, second_year, third_year, fourth_year, fifth_year, sixth_year,))
    db.commit()


def rup_statistic_query():
    now = datetime.datetime.now().date()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 0 AND 299999")
    first_day = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 300000 AND 699999")
    second_day = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 700000 AND 999999")
    third_day = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 1000000 AND 1499999")
    fourth_day = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 1500000 AND 1999999")
    fifth_day = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 2000000 AND 4999999")
    sixth_day = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 5000000 AND 9999999")
    first_month = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 10000000 AND 19999999")
    second_month = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 20000000 AND 29999999")
    third_month = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 30000000 AND 39999999")
    fourth_month = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 40000000 AND 49999999")
    fifth_month = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 50000000 AND 84999999")
    sixth_month = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 85000000 AND 119999999")
    first_year = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 120000000 AND 239999999")
    second_year = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 240000000 AND 359999999")
    third_year = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 360000000 AND 479999999")
    fourth_year = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup BETWEEN 480000000 AND 599999999")
    fifth_year = cur.fetchone()
    cur.execute("SELECT COUNT (*) from appart_apartment WHERE price_rup >= 600000000")
    sixth_year = cur.fetchone()
    params = [now] + [x[0] if x is not None else 0 for x in (
        first_day, second_day, third_day, fourth_day, fifth_day, sixth_day, first_month, second_month,
        third_month, fourth_month, fifth_month, sixth_month, first_year, second_year, third_year,
        fourth_year, fifth_year, sixth_year
    )]
    cur.execute(f'INSERT INTO statistic_pricerupstatistic (date, first_day, second_day, third_day, fourth_day, '
                f'fifth_day, sixth_day, first_month, second_month, third_month, fourth_month, fifth_month, '
                f'sixth_month, first_year, second_year, third_year, fourth_year, fifth_year, sixth_year) '
                f'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                params)
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
    cur.execute("SELECT COUNT(*) as total_result FROM appart_apartment")
    total_result = cur.fetchone()
    cur.execute("SELECT COUNT(*) as daily_result FROM appart_apartment WHERE DATE(date) = DATE(NOW())")
    daily_result = cur.fetchone()

    daily_result = daily_result[0] if daily_result else 0
    cur.execute("INSERT INTO statistic_adsstatistic (date, total, daily) VALUES (%s, %s, %s)",
                (now, total_result[0], daily_result))
    db.commit()


def google_sheets():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        '/Users/caramba/PycharmProject/BaliAdmin/json/villabot-382008-e3b439d175c9.json', scope)
    client = gspread.authorize(creds)
    sheet_url = "https://docs.google.com/spreadsheets/d/169LhrSJTHiUd-jFCS23nuoe-9dufI2WeubEHfq_kfKs"
    sh = client.open_by_url(sheet_url)
    now = datetime.datetime.now().date()
    cur.execute(f"SELECT * FROM statistic_commonstatistic WHERE date = '{now}'")
    common_stats = cur.fetchone()

    cur.execute(f"SELECT * FROM statistic_apartstatistic")
    apart_stats = cur.fetchall()

    cur.execute(f"SELECT * FROM statistic_locationstatistic WHERE date = '{now}'")
    location_stats = cur.fetchone()

    cur.execute(f"SELECT * FROM statistic_priceusdstatistic WHERE date = '{now}'")
    price_usd_stats = cur.fetchone()

    cur.execute(f"SELECT * FROM statistic_pricerupstatistic WHERE date = '{now}'")
    price_rup_stats = cur.fetchone()

    cur.execute(f"SELECT * FROM statistic_adsstatistic WHERE date = '{now}'")
    ads_stats = cur.fetchone()

    common_worksheet = None
    location_worksheet = None
    price_usd_worksheet = None
    price_rup_worksheet = None
    ads_worksheet = None
    apart_stats_worksheet = None

    cur.execute("SELECT COUNT (*) from appart_apartment")
    count = cur.fetchone()

    for worksheet in sh.worksheets():
        if worksheet.title == 'Common Statistics':
            common_worksheet = worksheet
        elif worksheet.title == 'Location Statistics':
            location_worksheet = worksheet
        elif worksheet.title == 'Price USD Statistics':
            price_usd_worksheet = worksheet
        elif worksheet.title == 'Price RUP Statistics':
            price_rup_worksheet = worksheet
        elif worksheet.title == 'Ads Statistics':
            ads_worksheet = worksheet
        elif worksheet.title == 'Apartment Statistics':
            apart_stats_worksheet = worksheet
    try:
        common_stats = [0 if x is None else x for x in common_stats]
    except IndexError:
        print("IndexError common stat")
    location_stats = [0 if x is None else x for x in location_stats]
    price_usd_stats = [0 if x is None else x for x in price_usd_stats]
    price_rup_stats = [0 if x is None else x for x in price_rup_stats]
    ads_stats = [0 if x is None else x for x in ads_stats]
    try:
        apart_stats = [0 if x is None else x for x in apart_stats]
    except IndexError:
        print("IndexError apart stat")

    if apart_stats_worksheet:
        for x in range(0, count[0]):
            try:
                row = [str(datetime.datetime.now().date()), apart_stats[x][6], apart_stats[x][1], apart_stats[x][2],
                       apart_stats[x][3],
                       apart_stats[x][4].strftime('%Y-%m-%d %H:%M:%S'), apart_stats[x][5].strftime('%Y-%m-%d %H:%M:%S')]
                apart_stats_worksheet.append_row(row)
            except IndexError:
                pass
            except TypeError:
                pass
    else:
        apart_stats_worksheet = sh.add_worksheet(title="Apartment Statistics", rows="100", cols="20")
        for x in range(0, count[0]):
            try:
                row = [str(datetime.datetime.now().date()), apart_stats[x][6], apart_stats[x][1], apart_stats[x][2],
                       apart_stats[x][3],
                       apart_stats[x][4].strftime('%Y-%m-%d %H:%M:%S'), apart_stats[x][5].strftime('%Y-%m-%d %H:%M:%S')]
                apart_stats_worksheet.append_row(row)
            except IndexError:
                pass
            except TypeError:
                pass
    if common_worksheet:
        common_worksheet.append_row([str(common_stats[1]), common_stats[2], common_stats[3], common_stats[4],
                                     common_stats[5], common_stats[6], common_stats[7], common_stats[8],
                                     common_stats[9]])
    else:
        common_worksheet = sh.add_worksheet(title="Common Statistics", rows="100", cols="20")
        common_worksheet.append_row(
            ['Common Statistics', str(common_stats[1]), common_stats[2], common_stats[3], common_stats[4],
             common_stats[5], common_stats[6], common_stats[7], common_stats[8], common_stats[9]])

    if location_worksheet:
        try:
            location_worksheet.append_row([str(location_stats[1]), location_stats[2]])
        except IndexError:
            pass
        except TypeError:
            pass
    else:
        location_worksheet = sh.add_worksheet(title="Location Statistics", rows="100", cols="20")
        location_worksheet.append_row(['Location Statistics', str(location_stats[1]), location_stats[2]])
    if price_usd_worksheet:
        price_usd_worksheet.append_row([str((price_usd_stats[1])), price_usd_stats[8],
             price_usd_stats[9], price_usd_stats[10], price_usd_stats[11], price_usd_stats[12], price_usd_stats[13],
             price_usd_stats[2], price_usd_stats[3], price_usd_stats[4], price_usd_stats[5], price_usd_stats[6],
             price_usd_stats[7], price_usd_stats[14], price_usd_stats[15], price_usd_stats[16], price_usd_stats[17],
             price_usd_stats[18],price_usd_stats[19]])
    else:
        price_usd_worksheet = sh.add_worksheet(title="Price USD Statistics", rows="100", cols="20")
        price_usd_worksheet.append_row(
            ['Price USD Statistics', str((price_usd_stats[1])), price_usd_stats[8],
             price_usd_stats[9], price_usd_stats[10], price_usd_stats[11], price_usd_stats[12], price_usd_stats[13],
             price_usd_stats[2], price_usd_stats[3], price_usd_stats[4], price_usd_stats[5], price_usd_stats[6],
             price_usd_stats[7], price_usd_stats[14], price_usd_stats[15], price_usd_stats[16], price_usd_stats[17],
             price_usd_stats[18], price_usd_stats[19]])
    if price_rup_worksheet:
        price_rup_worksheet.append_row([str((price_rup_stats[1])), price_rup_stats[2], price_rup_stats[3],
             price_rup_stats[4], price_rup_stats[5], price_rup_stats[6], price_rup_stats[7], price_rup_stats[8],
             price_rup_stats[9], price_rup_stats[10], price_rup_stats[11], price_rup_stats[12], price_rup_stats[13],
             price_rup_stats[14], price_rup_stats[15],price_rup_stats[16], price_rup_stats[17], price_rup_stats[18],
             price_rup_stats[19]])
    else:
        price_rup_worksheet = sh.add_worksheet(title="Price RUP Statistics", rows="100", cols="20")
        price_rup_worksheet.append_row(
            ['Price RUP Statistics', str((price_rup_stats[1])), price_rup_stats[2], price_rup_stats[3],
             price_rup_stats[4], price_rup_stats[5], price_rup_stats[6], price_rup_stats[7], price_rup_stats[8],
             price_rup_stats[9], price_rup_stats[10], price_rup_stats[11], price_rup_stats[12], price_rup_stats[13],
             price_rup_stats[14], price_rup_stats[15],price_rup_stats[16], price_rup_stats[17], price_rup_stats[18],
             price_rup_stats[19]])
    if ads_worksheet:
        ads_worksheet.append_row([(str(ads_stats[1])), ads_stats[2], ads_stats[3]])
    else:
        ads_worksheet = sh.add_worksheet(title="Ads Statistics", rows="100", cols="20")
        ads_worksheet.append_row([(str(ads_stats[1])), ads_stats[2], ads_stats[3]])
